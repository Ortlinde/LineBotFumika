//#region 全域引用
const auth = require('./JSON/config.json');
const request = require('request');
//#endregion

//#region 宣告請求
const baseExcel = {
    'method': 'GET',
    'url': auth.Gas.Get[0].baseExcel,
    'headers': {}
};
//#endregion

//#region 傳送請求
exports.getBaseExcel = function(userTalk, callback) {
    let backValue = new Array;
    request(baseExcel, function(error, response) {
        try {
            if (error) {
                callback(error);
            } else {
                const data = JSON.parse(response.body); //接收回傳(response)的body
                const keysValue = Object.keys(data); //將JsonObject的key值輸出成Array
                //迴圈判斷是否符合
                for (let i = 0; i < keysValue.length; i++) {
                    if (data[keysValue[i]].NAME === userTalk) {
                        callback(data[keysValue[i]].VALUE); //正確回傳結果
                    }
                }
                callback(false);
            }
        } catch (err) {
            console.log('getBaseExcelError', err);
            callback('getBaseExcelError');
        }
    });
};

//#endregion