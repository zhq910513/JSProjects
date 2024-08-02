_cookie = 'bm_sz=87732C82A314F08D3EA32EFF3CD63835~YAAQ72+bGwhGf/6QAQAAB5nDBxhxFBFCvUPM7uIp6nFu3b0YS+Serws+TD0QvgVKV/3fIajR1bilSlnifKiYnuadztBB369Al5scLq1G/YYemqtmAT74poCHkGyKbO8sqRvHmXwCUBXmEg7cDi87CP1lHTmamnI+MNf2U9hC//B3jCF++K0XXR2vivC4pBd6j2eAW4jJ+eFtbMv0mkDTinEbFppY6PxVel9/+J5bjL8DHXVgbcSn4FTwE5HQGPYUi/DkCraE3hxfvvEskLV4DOUv+XSSb2neiamRqCUGdQuX8eG+tDCNzxFGDWF1OmdOkIvm5nfJ0j02gtL2VYglvMB79cvlToneKqtojWETCp/4qzt3aoHdrWHoE958ABPGGzeXBGAWET2Bq6kpr+K7K0PhYxAwG3EMH5rTqF3JPJHA~3422516~4535364; _abck=06A99521992523E0F7D590422CB229C2~-1~YAAQ72+bGwpGf/6QAQAAy5vDBwz8pacqDdBWZwFycCofAGvNcX7ur466S8pIJDLh8Q2tbtGJaLhbVdWOOTsL/aIJ+GrR/lb7gSsb9f7voETb7X9CP88XWuSqXFEAngAaspa1raSdpfdCTN6rqa0uGcM05/sFOti5YGibtHrqTb7tVoej1yB5YH3f2Nox2/jiuQadVc2M7oph9XmL+nbijlP6iviC/EJapMPqzm+KaoLNHWdNuWSUkhcGPl6p3W14R9xLdI0aVr7kSvEHxdTqOUcHI3SP4/VGtBIl1ZPAjDj5Ki9mQfMMXIHnj/sKT2CnPQzajy4yjWpEYmjqy/MfNi2o07vDiTdk6DvMSKYsss8lWCnY9S74huvGHnmsRtRvrn+8AWHe+tNviycIxFVW55NV3LfxmXV9BB1s2aHmb8kLFmU3~-1~-1~-1; ak_bmsc=9ADDC1EB5AA3D6519237FAFEC9A6484A~000000000000000000000000000000~YAAQ72+bGw5Gf/6QAQAAC57DBxi0mpqZtMr3FytySgYn19RKNngHzyS/PC0ONAMinGB51mdV9XcBVoyUbiowcnEFwlJqp7vUT1UQ5SqwFl4Ib5Fa2LwfGAmnK/bGZKF8TGvu3orxyr0dOEWPqP7jNDHtX/SbiNUZHjN7fcR4KTqfF3lwDUyj3suyUpBAj+n0f4vs4Bo1neJlAaS6eLz+psH2I+zczYjNTSTQur+L5YKIZkXruPom/igGThCemxJT/GYzm8lddZD4ite700ncL7TC2TfE7xM1uEa2efaYqowGgN0Dd9vNOOt6izHd9XKJEVgbBKPkSapEKlT8HDZVhq5uLEAuXp9rcl1njMV9O83XRIGFhmENyQ5CJbTRkReCrLbhTIfbafgonZXuVbjZbWkfY/zV1uIpNtg2RoaiatcgA5atagN4zEMfkIdzuM1/KCMvqpI=';

// 检查 navigator 属性
_navigator = {
    credentials: true,
    appMinorVersion: false,
    bluetooth: true,
    storage: true,
    getGamepads: true,
    getStorageUpdates: false,
    hardwareConcurrency: true,
    mediaDevices: true,
    mozAlarms: false,
    mozConnection: false,
    mozIsLocallyAvailable: false,
    mozPhoneNumberService: false,
    msManipulationViewsEnabled: false,
    permissions: true,
    registerProtocolHandler: true,
    requestMediaKeySystemAccess: true,
    requestWakeLock: false,
    sendBeacon: true,
    serviceWorker: true,
    storeWebWideTrackingException: false,
    webkitGetGamepads: false,
    webkitTemporaryStorage: true,

};

start_time = Date.now();
fn = {
    "fpValStr": "-1",
    "rVal": "-1",
    "rCFP": "-1",
    "td": -999999
};
t4 = [
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
BXO = parseInt(KS(start_time, t4[37]), 10);
qQ = parseInt(KS(BXO, 23), 10);
Xn = _abck(_cookie);
MQ = DQ(start_time);

function random_time() {
    return Math.floor(Math.random() * 2001) + 3000;
}

function KS(a, b) {
    return a / b;
}

function qS(a, b) {
    return a - b;
}

function bc(a, b) {
    return a + b;
}

function LS(a, b) {
    return a << b;
}

function BN(_abck) {
    for (var UmO = 0, mmO = 0; mmO < _abck.length; mmO++) {
        var bmO = _abck['charCodeAt'](mmO);
        bmO < 128 && (UmO += bmO);
    }
    return UmO;
}

function hQ() {
    return bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(bc(Boolean(_navigator.credentials), LS(Boolean(_navigator.appMinorVersion), 1)), LS(Boolean(_navigator.bluetooth), 2)), LS(Boolean(_navigator.storage), 3)), LS(Boolean(Math.imul), 4)), LS(Boolean(_navigator.getGamepads), 5)), LS(Boolean(_navigator.getStorageUpdates), 6)), LS(Boolean(_navigator.hardwareConcurrency), 7)), LS(Boolean(_navigator.mediaDevices), 8)), LS(Boolean(_navigator.mozAlarms), 9)), LS(Boolean(_navigator.mozConnection), 10)), LS(Boolean(_navigator.mozIsLocallyAvailable), 11)), LS(Boolean(_navigator.mozPhoneNumberService), 12)), LS(Boolean(_navigator.msManipulationViewsEnabled), 13)), LS(Boolean(_navigator.permissions), 14)), LS(Boolean(_navigator.registerProtocolHandler), 15)), LS(Boolean(_navigator.requestMediaKeySystemAccess), 16)), LS(Boolean(_navigator.requestWakeLock), 17)), LS(Boolean(_navigator.sendBeacon), 18)), LS(Boolean(_navigator.serviceWorker), 19)), LS(Boolean(_navigator.storeWebWideTrackingException), 20)), LS(Boolean(_navigator.webkitGetGamepads), 21)), LS(Boolean(_navigator.webkitTemporaryStorage), 22)), LS(Boolean(Number.parseInt), 23)), LS(Boolean(Math.hypot), 24));
}

function DQ(KUO) {
    for (var wUO = Math.floor(1e5 * Math.random() + 1e4), LUO = (KUO * wUO).toString(), kUO = 0, HUO = [], SUO = LUO.length >= 18; HUO.length < 6;)
        HUO.push(parseInt(LUO['slice'](kUO, kUO + 2), 10)),
            kUO = SUO ? kUO + 3 : kUO + 2;
    return [wUO, function IUO(sUO) {
        var pUO = sUO[0] - sUO[1];
        var nUO = sUO[2] - sUO[3];
        var QUO = sUO[4] - sUO[5];
        var WUO = Math.sqrt(pUO * pUO + nUO * nUO + QUO * QUO);
        return Math.floor(WUO);
    }(HUO)];
}

function _abck(cookie) {
    if (cookie)
        for (var QCO = '_abck=', NCO = cookie.split("; "), rCO = 0; rCO < NCO.length; rCO++) {
            var xCO = NCO[rCO];
            if (0 === xCO['indexOf'](QCO)) {
                var RCO = xCO['substring'](QCO['length'], xCO['length']);
                if (-1 !== RCO['indexOf']("~") || -1 !== (OO['decodeURIComponent'](RCO))['indexOf']("~")) {
                    return RCO;
                }
            }
        }
}

function array_25() {
    return [
        1,
        32,
        32,
        0,
        0,
        0,
        0,
        random_time(), // 时间差,
        0,
        start_time,
        fn['td'],
        parseInt(KS(BXO, 23), 10),
        0,
        0,
        parseInt(KS(qQ, 6), 10),
        0,
        0,
        random_time(), // 时间差,
        0,
        '0',
        Xn,
        BN(Xn),
        fn['rVal'],
        fn['rCFP'],
        hQ(),
        'PiZtE',
        MQ[0],
        MQ[1],
        '0',
        '0',
        0,
        ',',
        '',
        '0'
    ]['join'](',')
}

console.log(array_25())