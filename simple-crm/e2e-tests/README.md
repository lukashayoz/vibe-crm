# E2E Testing with Playwright

This directory contains end-to-end tests for the Simple CRM application using Playwright.

## Test Design Philosophy

The tests are designed to verify the structure and functionality of the application rather than specific content. This approach allows the same tests to be used in different environments (development, staging, production) regardless of the actual data present in the database.

### What we test:
- Page structure (headers, tables, forms)
- Navigation between pages
- Data structure and formatting (not specific values)
- Form submission and validation

### What we don't test:
- Specific data values that may change between environments
- Implementation details that could change without affecting functionality

## Running Tests in Different Environments

### Development Environment

```bash
# Install dependencies
npm install
npx playwright install --with-deps chromium

# Run tests against local development server
npm run test:e2e
```

### CI Environment

Tests run automatically on GitHub Actions for pull requests and pushes to main. The workflow:
1. Sets up the test database
2. Starts the application server
3. Runs the tests
4. Uploads test reports as artifacts

### Production Environment

To run tests against a production environment:

```bash
# Set the base URL to your production environment
BASE_URL=https://your-production-url.com npm run test:e2e
```

## Customizing Tests for Different Environments

If you need to run environment-specific tests, you can use Playwright's test.skip() or test.only() with environment conditions:

```javascript
// Example: Skip a test in production
const isProd = process.env.NODE_ENV === 'production';
test.skip(isProd, 'should create a new lead (skipped in production)')('test description', async ({ page }) => {
  // Test code
});
```