// 环境检测点
_window = {
    addEventListener: true,
    XMLHttpRequest: true,
    XDomainRequest: true,
    emit: true,
    DeviceOrientationEvent: true,
    DeviceMotionEvent: true,
    TouchEvent: true,
    spawn: true,
    chrome: {
        webstore: undefined,
    },
    Buffer: true,
    PointerEvent: true,
    innerWidth: true,
    outerWidth: true,
    HTMLElement: true,
    RTCPeerConnection: true,
    webkitRTCPeerConnection: true,
    FileReader: true,

    callPhantom: false,
    ActiveXObject: false,
    mozRTCPeerConnection: false,

    opera: undefined,
    mozInnerScreenY: false,

};
_Function = {
    prototype: {
        bind: true
    }
};
_document = {
    documentMode: undefined,

};
_navigator = {
    onLine: true,
    vibrate: true,
    getBattery: true,

};
_InstallTrigger = false;
_Array = {
    prototype: {
        forEach: true,
    }
};

// 固定变量
// 变化变量
start_time = Date.now();

// 公用方法
function KS(a, b) {
    return a / b;
}

function bc(a, b) {
    return a + b;
}

function Cr(a, b) {
    return a * b;
}

function BN(a) {
    for (var b = 0, c = 0; c < a.length; c++) {
        var d = a['charCodeAt'](c);
        d < 128 && (b += d);
    }
    return b;
}

// 数组值
function array_1() {
    var t4 = [
        4095,
        1040,
        300000,
        0,
        3,
        20,
        70,
        1,
        11,
        14,
        19,
        22,
        23,
        27,
        29,
        8888888,
        7777777,
        10,
        1000,
        10000,
        25,
        8,
        2,
        100,
        9,
        999999,
        4,
        13,
        21,
        3600000,
        24,
        65535,
        65793,
        4294967295,
        4282663,
        8388607,
        32,
        4064256,
        12,
        2048,
        3540,
        90,
        3000
    ];

    var user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36';
    var SjO = "".concat(BN(user_agent));
    var cjO = parseInt(KS(start_time, 2));

    var BXO = parseInt(KS(start_time, t4[37]), t4[17]);
    var PXO = Math.random();
    var EXO = parseInt(KS(Cr(1000, PXO), t4[22]), 10);
    fXO = "".concat(PXO);
    var fXO = bc(fXO.slice(0, 11), EXO);

    var func_1 = 12147;
    var func_2 = ',cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1';

    return (((((((((((((((((((((((('')['concat'](user_agent, ',uaend,'))['concat'](func_1, ','))['concat']('20030107', ','))['concat']('zh-CN', ','))['concat']('Gecko', ','))['concat'](5, ','))['concat'](0, ','))['concat'](0, ','))['concat'](0, ','))['concat'](BXO, ','))['concat'](0, ','))['concat'](1440, ','))['concat'](912, ','))['concat'](1440, ','))['concat'](960, ','))['concat'](1440, ','))['concat'](791, ','))['concat'](1440, ','))['concat'](func_2, ','))['concat'](SjO, ','))['concat'](fXO, ','))['concat'](cjO, ','))['concat'](0, ','))['concat'](1, ',loc:');
}

console.log(array_1())
