let content = "{qqq.GNyYBRH1O4sz8vh6QSHW6DM8nmdtn4p_CiTjJA_fiWl|[YTaXFuVHJAy7xbqcrAWvKs3zM2Q8WDa.iPEGxpJ1Jm7QUPW4RSNfWKaWROzPr1rcElVEsSgAxrL5skgwxrV5ApJcrnLOifzmqffP5f.yMilXyrCdoQ9XuA6.qiZignI8HWL9n1i0D5qKzkuOJB7SenkZHBEedckuMJllnSUMoBRbuOkbJwJG0Dn.r7ErTpMbJQ0MZf4DMiZ10kBMH73G9s1mlwAwTScMR52yTkoVRLpGfvv8xEgubroHoQEAODIZ8wZSCKFh3EzyT1s4HRR95utyJRWozCunx30p.KDOD3RP51I6qhVcjKtTEyA_XDaqqqqqqr1Qi_LWbGC1kyLxvAtIcxZiGqimqLQEqqVxT9KMfY.mKaKMfY9lbGV 0wR7HvJ6IsUC410DntKRngA;QyqA82EGtIB6ePNEeYo9NG;iEm6gdSTTpYiqU10OlvsnG;yMG8gk5okQ97gP4eb.IadA;T8F36FaS9AtR4sXBkRr0iG;RTlM3IYjAzboXbIiNSIFRA;t7_svh3Kc3.VU9jOjAJgdq;.8D9Zx78FrKF.Zn4xbfmIG;IMhCM7gXESIqShs5TNMo9A;pvBPF7OtrK6trS5vZYizwa;9qxqLXuEeDQeAlNfAL_l.A;VNeyFcNDtQZhV2sfCxyHqA;kT4JL2WRSOhvUIEcOjSrva;LpFhLGWYI8eFx_X999MLEq;NqssQaVItFB0TevtNxJrkG;AI3RN3R7lP0BBnYsoCO5KG;xrYRhwM6FYW7zCsPL.iecq;0kOXzZzt1eXLrlPo.QQ4xG;ApKNqLIRoybF5rIxSnabBG;hfgZrtz_KscdFC6a3f1wKA;qqr0c80qql3650Ddfe167qqr4{6KT2N3Cyj3sV_tOE_iPL0hUVUHGWacnZuHf3LkcG1HG9BinZDtA7ZkOz83Y2.Yc9ttGVnquyQirEgokgYF9SNAClKiGZnosLHJqyTksQhHr3TZ6UzHXaZeuWqqr0m26649qql4096qqqhjZjSisUVLjXkryQq!x7z,aac,amr,asm,avi,bak,bat,bmp,bin,c,cab,css,csv,com,cpp,dat,dll,doc,dot,docx,exe,eot,fla,flc,fon,fot,font,gdb,gif,gz,gho,hlp,hpp,htc,ico,ini,inf,ins,iso,js,jar,jpg,jpeg,json,java,lib,log,mid,mp4,mpa,m4a,mp3,mpg,mkv,mod,mov,mim,mpp,msi,mpeg,obj,ocx,ogg,olb,ole,otf,py,pyc,pas,pgm,ppm,pps,ppt,pdf,pptx,png,pic,pli,psd,qif,qtx,ra,rm,ram,rmvb,reg,res,rtf,rar,so,sbl,sfx,swa,swf,svg,sys,tar,taz,tif,tiff,torrent,txt,ttf,vsd,vss,vsw,vxd,woff,woff2,wmv,wma,wav,wps,xbm,xpm,xls,xlsx,xsl,xml,z,zip,apk,plist,ipak162Hle0P4nhLEiQ2Tc3q}!ruG4VK2xQ9gvs6yW3Gq2YbyM3nYN3nQ.36g2DTGjF1NLxbWUKD7vxD3b3vl2tP9zWAxHW6ZKVOe0J2lwAKRWh6qSKkSbcmJN1pSellaawSwPim0Fs2xxWkVmJGzKEDGOFfyCkOVbVuYSEVEZp2Y.rm38Yp9TrVxkwOw6oOlJFpJwoURFxaebmvE8i2yismxxUpfxZsIvJBJNTvsH3QRbZlkbxM3t10747904321EaaWRVTNpv3JRTwesaqqhFUDuA6FHxp.K8yJQ_FxFWQ8HfE.gWZNemAqqr0lmJl4qqhasVtJBf6njXqqqYQQdnQS2LcJZxKSvK9DOIi|g1MrePq.9qwTy4kOUHQEI5uckkHlXurdCi8Gy_nM9tea36GDHkgy4OunshFLq9P_BWyAFXq8kq4zedGFLIEaj9U_bk3AEzfDoHxGQLSPg8.q3fq6NrLLIerbpoRLr.fihmNqyLs5sHMqKXuu1oE0DXUCKDJaMf1FRo40cjPHFtx9h26D1QxWQ21_cHh2_.u6DiEQFjv5ArxReXA_2xEzeXsnFluq.81wUlmq1wpSSrClkIfx3kCE811ev8lLeMn2txU0NAS2utTLMKGedET2d362Y8U3D1veaIC0J";

// 1、补充 window 对象
window = global;

// 网站会检测 "__filename"/"__dirname" 关键字是否可用，来判断是否为真实的浏览器环境
delete __filename;
delete __dirname;

// 补充 window 对象下其他需要的环境
null_function = function (){
    console.log("--- args ---", ...arguments)
}
setTimeout = null_function;
setInterval = null_function;
window.top = window;
window.addEventListener = function (res1, res2, res3) {
    console.log("当前执行 window 当中的 addEventListener 方法：", res1, res2, res3);
};
window.attachEvent = function (res1, res2) {
    console.log("当前执行 window 当中的 attachEvent 方法：", res1, res2);
};

// 2、补充 document 对象
div = {
    getElementsByTagName: function (res) {
        console.log("当前执行 div 当中的 getElementsByTagName 方法：", res);
        if (res === "i") {
            return {}
        }
    }
};
meta = [
    {
        getAttribute: function (res) {
            console.log("当前执行 meta 当中的 getAttribute 方法：", res);
            if (res === "r") {
                return "m"
            }
        },
        content: content,
        parentNode: {
            removeChild: function (res) {
                console.log("当前执行 meta 当中的 removeChild 方法：", res);
            }
        }
    }
];
script = [
    {
        type: "text/javascript",
        getAttribute: function (res) {
            console.log("当前执行 script 当中的 getAttribute 方法：", res);
            if (res === "r") {
                return "m"
            }

            console.log("当前执行 script 当中的 getAttribute 方法  *缺失*：", res);
        },
        parentElement: {
            removeChild: function (res) {
                console.log("当前执行 script 当中父节点的 removeChild 方法：", res);
            }
        }
    }
];
document = {
    createElement: function (res) {
        console.log("当前执行 document 当中的 createElement 方法：", res);
        if (res === "div") {
            return div;
        }
    },
    getElementsByTagName: function (res) {
        console.log("当前执行 document 当中的 getElementsByTagName 方法：", res);
        if (res === "meta") {
            return meta
        }
        if (res === "script") {
            return script
        }
        console.log("当前执行 document 当中的 getElementsByTagName *** 缺失方法 ***：", res);
    },
    addEventListener: function (res1, res2, res3) {
        console.log("当前执行 window 当中的 addEventListener 方法：", res1, res2, res3);
    },
    attachEvent: function (res1, res2) {
        console.log("当前执行 window 当中的 attachEvent 方法：", res1, res2);
    },
};

// 3、补充 navigator 对象
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

// 4、补充 location 对象
location = {
    "ancestorOrigins": {},
    "href": "http://www.fangdi.com.cn/index.html",
    "origin": "http://www.fangdi.com.cn",
    "protocol": "http:",
    "host": "www.fangdi.com.cn",
    "hostname": "www.fangdi.com.cn",
    "port": "",
    "pathname": "/index.html",
    "search": "",
    "hash": ""
};

// 5、补充 screen 对象

// 6、补充 localStorage 对象


// ====================================================   代理吐环境   ===================================================
require("../../../../环境检测框架/proxy吐环境")