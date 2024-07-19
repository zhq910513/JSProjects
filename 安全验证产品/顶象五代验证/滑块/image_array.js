let r = "include"
    , o = "s"
    , t = "h";

function i(n) {
    if (!n)
        return "";
    let output = "";
    let r = 43746;

    for (let o = 0; o < n.length; o++) {
        const t = n.charCodeAt(o); // 获取字符的Unicode编码
        const i = t ^ r; // 对字符编码进行异或操作
        r = t; // 更新r为当前字符编码
        output += String.fromCharCode(i); // 将异或后的编码转换为字符并添加到输出中
    }
    return output
}

function a(n, e) {
    for (let t = [1, 0, 2], i = 0; ;) {
        switch (t[i++]) {
            case 0:
                let a = 0, c = n.length;
                for (; a < c; a++)
                    if (n[a] === e)
                        return !0;
                continue;
            case 1:
                if (n[[r, o].join("")])
                    return n.includes(e);
                continue;
            case 2:
                return !1
        }
        break
    }
}

function get_array(n) {
    let r = [];
    let e = "pus";
    let o = 0;
    for (; o < n[i("\uaa8e\uaaeb\uaa85\uaae2\uaa96\uaafe")]; o++) {
        let c = n.charCodeAt(o);
        if (32 === o)
            break;
        for (; a(r, c % 32);)
            c++;
        r[[e, t].join("")](c % 32)
    }
    return r
}