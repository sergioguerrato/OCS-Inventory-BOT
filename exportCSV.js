require('dotenv').config()
const puppeteer = require('puppeteer');
const path = require('path');

console.log('Bem vindo ao Bot-OCS');

(async() => {

  // Set Delay Func
  function delay(time) {
    return new Promise(function(resolve) { 
        setTimeout(resolve, time)
    });
  }

  // Launch the browser and open a new blank page
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // Navigate the page to a URL
  await page.goto('http://10.0.0.21/ocsreports/?function=visu_computers');

  // Set username
  await page.type('[name="LOGIN"]', 'admin');

  // Set password
  await page.type('[name="PASSWD"]', '1234');

  // Submit info and wait for data load
  await page.click('[type="submit"]');

  await delay(2000);
  // Select bot-ocs Layout
  await page.click('#layout')
  await page.keyboard.press('ArrowDown');
  await page.keyboard.press('Enter');

  await delay(2000);
  // Sort for latest date show first
  await page.click('[class="lastdate sorting"]');

  await delay(2000);
  // First try, download the export file
  //await page.downloadPath('C:\Users\supor\Desktop\OCS-Inventory-BOT');
  await page.click('#list_show_all_csv_total > a');

  await delay(5000);
  await browser.close();
})();
