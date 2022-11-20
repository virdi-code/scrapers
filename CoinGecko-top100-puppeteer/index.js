
const pup = require('puppeteer');
const fs = require('fs');
// functions
// page.screenshot
// page.pdf
// page.content
// page.evaluate


async function scrape(){
    const instance = await pup.launch();
    const page = await instance.newPage();
    await page.goto('https://www.coingecko.com/');

    const rows = await page.evaluate(()=>
        Array.from(document.querySelectorAll('tbody tr'),e=>({
            
            coin : e.querySelector('span').innerText,
            sym : e.querySelector('span').nextElementSibling.innerText, 
            price :e.querySelector('.td-price').innerText.replace('Buy\n',''), 
            ch24 : e.querySelector('.change24h').innerText,  
            ch7d : e.querySelector('.change7d').innerText,  
            vol24 : e.querySelector('.td-liquidity_score').innerText,
            fdv : e.querySelector('.td-fdv').innerText.trim(),
            mcap : e.querySelector('.td-market_cap').innerText, 

        }))
    )
    console.log(rows)
    var file_name = new Date().getTime()
    fs.writeFile(file_name + ".json",JSON.stringify(rows),(err)=>{
        if(err) throw err;
        console.log("File Saved")
    })
    instance.close();
}

scrape();
