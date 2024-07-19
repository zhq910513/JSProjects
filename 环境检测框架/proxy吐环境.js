function SetProxy(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
            get: function (target, property, receiver) {
                if (property !== "Math" && property !== "isNaN") {
                    if (target[property] && typeof target[property] != "string" && Object.keys(target[property]).length > 3) {
                        // Do nothing if the condition is met
                    } else {
                        console.log(
                            "方法：get",
                            "   ",
                            "对象：", proxyObjs[i],
                            "   ",
                            "属性：", property,
                            "   ",
                            "属性类型：", typeof property,
                            "   ",
                            "属性值：", target[property]
                        );
                        // if (target[property] === undefined){
                        //     console.log(
                        //         "方法：get",
                        //         "   ",
                        //         "对象：", proxyObjs[i],
                        //         "   ",
                        //         "属性：", property,
                        //         "   ",
                        //         "属性类型：", typeof property,
                        //         "   ",
                        //         "属性值：", target[property]
                        //     );
                        // }
                    }
                }
                return target[property];
            },

            set: function (target, property, value, receiver) {
                console.log(
                    "方法：set",
                    "   ",
                    "对象：", proxyObjs[i],
                    "   ",
                    "属性：", property,
                    "   ",
                    "属性类型：", typeof property,
                    "   ",
                    "属性值：", value,
                    "   ",
                    "属性值类型：", typeof target[property]
                );
                return Reflect.set(target, property, value, receiver);
            },
        }`;

        eval(`try {
            ${proxyObjs[i]};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        } catch (e) {
            ${proxyObjs[i]} = {};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        }`)
    }
}

const proxy_array = [
    'window',
    'document',
    'location',
    'navigator',
    'history',
    'screen',
    'localStorage',
    'sessionStorage',
    'aaa',
    'target'
];
SetProxy(proxy_array)
