const { test, expect } = require('@playwright/test');

test.describe('Leads page tests', () => {
  test('should display leads list with correct data', async ({ page }) => {
    // Go to the leads page
    await page.goto('/leads');
    
    // Check page title
    await expect(page).toHaveTitle('Leads - Simple CRM');
    
    // Check page heading
    const heading = page.locator('h1');
    await expect(heading).toHaveText('Leads');
    
    // Check if the table is present
    const table = page.locator('table.table');
    await expect(table).toBeVisible();
    
    // Check table headers
    const headers = page.locator('thead th');
    await expect(headers).toHaveCount(4);
    
    // Check specific header texts 
    await expect(headers.nth(0)).toHaveText('ID');
    await expect(headers.nth(1)).toHaveText('Title');
    await expect(headers.nth(2)).toHaveText('Amount');
    await expect(headers.nth(3)).toHaveText('Created');
    
    // Check if there are leads in the table
    const rows = page.locator('tbody tr');
    
    // There should be at least our two test leads
    await expect(rows).toHaveCount(2); 
    
    // Check for specific test data from our test fixtures
    // Look for specific text in the lead titles
    const leadTitles = page.locator('tbody tr td:nth-child(2)');
    await expect(leadTitles.first()).toContainText('Test Lead 1');
    await expect(leadTitles.nth(1)).toContainText('Test Lead 2');
    
    // Check for amount formatting with dollar sign
    const leadAmounts = page.locator('tbody tr td:nth-child(3)');
    await expect(leadAmounts.first()).toContainText('$1000');
  });
  
  test('navigation from homepage to leads page works', async ({ page }) => {
    // Start at homepage
    await page.goto('/');
    
    // Click on the Leads link in the navigation
    await page.click('text=Leads');
    
    // Verify that we're on the leads page
    await expect(page).toHaveURL('/leads');
    await expect(page).toHaveTitle('Leads - Simple CRM');
    
    // Verify the leads table is visible
    const table = page.locator('table.table');
    await expect(table).toBeVisible();
  });
});