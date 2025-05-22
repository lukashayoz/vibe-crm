const { test, expect } = require('@playwright/test');

test.describe('Leads page tests', () => {
  test('should display leads list with correct structure', async ({ page }) => {
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
    
    // Check header structure - these should be consistent across environments
    await expect(headers.nth(0)).toHaveText('ID');
    await expect(headers.nth(1)).toHaveText('Title');
    await expect(headers.nth(2)).toHaveText('Amount');
    await expect(headers.nth(3)).toHaveText('Created');
    
    // Check if there are leads in the table - at least one row should exist
    const rows = page.locator('tbody tr');
    await expect(rows).toHaveCount({ minimum: 1 }); 
    
    // Check data structure rather than specific content
    // Verify lead ID is numeric
    const firstLeadId = await page.locator('tbody tr td:nth-child(1)').first().textContent();
    expect(Number.isInteger(Number(firstLeadId.trim()))).toBeTruthy();
    
    // Verify lead title exists and is non-empty
    const firstLeadTitle = await page.locator('tbody tr td:nth-child(2)').first().textContent();
    expect(firstLeadTitle.trim().length).toBeGreaterThan(0);
    
    // Verify amount has currency formatting (contains $ symbol)
    const firstLeadAmount = await page.locator('tbody tr td:nth-child(3)').first().textContent();
    expect(firstLeadAmount.includes('$')).toBeTruthy();
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