
import asyncio
import json
import os
import re
from playwright.async_api import async_playwright, expect

async def test_scenario_1_initial_load(page):
    print("\n--- Running Scenario 1: Initial Load ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    await expect(page.locator("#progress")).to_have_text("1 / 415")
    await expect(page.locator("#actions")).to_have_css("opacity", "0")
    await expect(page.locator("#error-badge")).to_have_text("0")
    print("✅ Scenario 1: Initial Load test passed.")

async def test_scenario_2_card_flip(page):
    print("\n--- Running Scenario 2: Card Flip ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    flashcard = page.locator("#flashcard")
    actions = page.locator("#actions")
    await expect(flashcard).not_to_have_class(re.compile(r"\bflipped\b"))
    await flashcard.click()
    await expect(flashcard).to_have_class(re.compile(r"\bflipped\b"))
    await expect(actions).to_have_css("opacity", "1")
    print("✅ Scenario 2: Card Flip test passed.")

async def test_scenario_3_umiem_button(page):
    print("\n--- Running Scenario 3: 'Umiem' Button ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    question = page.locator("#card-question")
    initial_question_text = await question.text_content()
    await page.locator("#flashcard").click()
    await page.locator("#btn-know").click()
    await expect(question).not_to_have_text(initial_question_text)
    await expect(page.locator("#progress")).to_have_text("2 / 415")
    print("✅ Scenario 3: 'Umiem' Button test passed.")

async def test_scenario_4_powtorze_button(page):
    print("\n--- Running Scenario 4: 'Powtórzę' Button ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    question = page.locator("#card-question")
    initial_question_text = await question.text_content()
    await page.locator("#flashcard").click()
    await page.locator("#btn-dont-know").click()
    await expect(question).not_to_have_text(initial_question_text)
    await expect(page.locator("#error-badge")).to_have_text("1")
    print("✅ Scenario 4: 'Powtórzę' Button test passed.")

async def test_scenario_5_review_mode(page):
    print("\n--- Running Scenario 5: 'Do powtórki' Mode ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    flashcard = page.locator("#flashcard")
    question = page.locator("#card-question")
    btn_know = page.locator("#btn-know")
    btn_dont_know = page.locator("#btn-dont-know")
    error_badge = page.locator("#error-badge")
    progress = page.locator("#progress")
    mode_errors = page.locator("#mode-errors")
    mode_all = page.locator("#mode-all")
    card_wrapper = page.locator("#card-wrapper")

    await flashcard.click(); await btn_dont_know.click()
    await expect(progress).to_have_text("2 / 415")
    await flashcard.click(); await btn_know.click()
    await expect(progress).to_have_text("3 / 415")
    await flashcard.click(); await btn_dont_know.click()
    await expect(progress).to_have_text("4 / 415")
    await expect(error_badge).to_have_text("2")

    await mode_errors.click()
    await expect(progress).to_have_text("1 / 2")

    review_card_1_text = await question.text_content()
    await flashcard.click(); await btn_know.click()
    await expect(question).not_to_have_text(review_card_1_text)
    await expect(progress).to_have_text("1 / 1")

    await flashcard.click(); await btn_know.click()
    await expect(card_wrapper).to_contain_text("Brak fiszek do powtórki!")
    
    await mode_all.click()
    await expect(progress).to_have_text("4 / 415")
    print("✅ Scenario 5: 'Do powtórki' Mode test passed.")

async def test_scenario_6_persistence(page):
    print("\n--- Running Scenario 6: State Persistence ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    question = page.locator("#card-question")
    btn_know = page.locator("#btn-know")
    progress = page.locator("#progress")
    first_card_text = await question.text_content()
    
    await page.locator("#flashcard").click()
    await btn_know.click()
    await expect(question).not_to_have_text(first_card_text)
    await expect(progress).to_have_text("2 / 415")
    
    question_before_reload = await question.text_content()
    
    await page.reload()
    await page.wait_for_load_state('networkidle')
    await expect(progress).to_have_text("2 / 415")
    await expect(question).to_have_text(question_before_reload)
    print("✅ Scenario 6: State Persistence test passed.")

async def test_scenario_7_reset_progress(page):
    print("\n--- Running Scenario 7: Reset Progress ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    question = page.locator("#card-question")
    btn_know = page.locator("#btn-know")
    btn_dont_know = page.locator("#btn-dont-know")
    btn_reset = page.locator("#btn-reset")
    error_badge = page.locator("#error-badge")
    progress = page.locator("#progress")
    
    first_card_text = await question.text_content()
    await page.locator("#flashcard").click(); await btn_know.click()
    await expect(question).not_to_have_text(first_card_text)

    second_card_text = await question.text_content()
    await page.locator("#flashcard").click(); await btn_dont_know.click()
    await expect(question).not_to_have_text(second_card_text)

    page.on("dialog", lambda dialog: dialog.accept())
    await btn_reset.click()
    
    await expect(progress).to_have_text("1 / 415")
    await expect(error_badge).to_have_text("0")
    
    state_storage_raw = await page.evaluate("localStorage.getItem('mistrz_state')")
    assert state_storage_raw is not None
    state_storage = json.loads(state_storage_raw)
    assert state_storage['index'] == 0
    print("✅ Scenario 7: Reset Progress test passed.")

async def test_scenario_8_mode_switching(page):
    print("\n--- Running Scenario 8: Mode Switching ---")
    await page.goto("file:///Users/marek/workspace/mistrz-polszczyzny/index.html")
    await page.wait_for_load_state('networkidle')
    
    flashcard = page.locator("#flashcard")
    question = page.locator("#card-question")
    btn_know = page.locator("#btn-know")
    btn_dont_know = page.locator("#btn-dont-know")
    progress = page.locator("#progress")
    mode_errors = page.locator("#mode-errors")
    mode_all = page.locator("#mode-all")
    card_wrapper = page.locator("#card-wrapper")

    # Go through 3 cards
    q1 = await question.text_content()
    await flashcard.click(); await btn_know.click()
    await expect(question).not_to_have_text(q1)
    
    q2 = await question.text_content()
    await flashcard.click(); await btn_dont_know.click()
    await expect(question).not_to_have_text(q2)

    q3 = await question.text_content()
    await flashcard.click(); await btn_know.click()
    await expect(question).not_to_have_text(q3)
    await expect(progress).to_have_text("4 / 415")

    card_4_text = await question.text_content()

    await mode_errors.click()
    await expect(progress).to_have_text("1 / 1")
    
    await flashcard.click()
    await btn_know.click()
    await expect(card_wrapper).to_contain_text("Brak fiszek do powtórki!")

    await mode_all.click()
    await page.wait_for_load_state('networkidle')
    
    await expect(progress).to_have_text("4 / 415")
    await expect(question).to_have_text(card_4_text)
    print("✅ Scenario 8: Mode Switching State test passed.")


async def main():
    headless = os.environ.get('HEADLESS', 'true').lower() != 'false'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        
        # Run all tests in sequence, with a new page for each
        page = await browser.new_page()
        await test_scenario_1_initial_load(page)
        await page.close()

        page = await browser.new_page()
        await test_scenario_2_card_flip(page)
        await page.close()

        page = await browser.new_page()
        await test_scenario_3_umiem_button(page)
        await page.close()

        page = await browser.new_page()
        await test_scenario_4_powtorze_button(page)
        await page.close()
        
        page = await browser.new_page()
        await test_scenario_5_review_mode(page)
        await page.close()

        page = await browser.new_page()
        await test_scenario_6_persistence(page)
        await page.close()

        page = await browser.new_page()
        await test_scenario_7_reset_progress(page)
        await page.close()

        page = await browser.new_page()
        await test_scenario_8_mode_switching(page)
        await page.close()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
