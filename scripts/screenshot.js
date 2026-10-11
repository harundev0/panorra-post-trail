const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1400, height: 1000 },
    deviceScaleFactor: 2, // High resolution for PPT
  });
  
  const page = await context.newPage();
  
  // Go to local file
  const filePath = `file://${path.resolve('tourmkr_ui.html')}`;
  console.log('Loading page:', filePath);
  await page.goto(filePath, { waitUntil: 'networkidle' });

  // Give Alpine and fonts some time to render
  await page.waitForTimeout(2000);

  // We want to screenshot the interactive prototype first
  console.log('Taking full page screenshot...');
  await page.screenshot({ path: 'Tourmkr_App_Flow.png', fullPage: true });

  // We can also take targeted screenshots of just the screen states
  console.log('Taking section screenshots...');
  
  // 1. Prototype section
  const prototypeSection = await page.locator('section:nth-of-type(1)');
  await prototypeSection.screenshot({ path: 'Tourmkr_Interactive_Proto.png' });

  // 2. Previews - Create Flow
  const previewsCreate = await page.locator('section:nth-of-type(2)');
  await previewsCreate.screenshot({ path: 'Tourmkr_Create_Post_Flow.png' });

  // 3. Previews - Detail 360 Flow
  const previewsDetails = await page.locator('section:nth-of-type(3)');
  await previewsDetails.screenshot({ path: 'Tourmkr_Detail_360_Flow.png' });

  console.log('Screenshots generated successfully!');
  await browser.close();
})();
