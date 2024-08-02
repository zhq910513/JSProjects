// AQ = YQ()(wI(BD, [vO.g8(Vk, BQ, bF, lc), OO[vO.Bl(1, pH, Wf, pk)].bmak[vO.CZ(UL(UL(1)), qL, jn, dS)], vO.l8(UL({}), lS, CF, PQ), ln, vO.Ud(UL(UL({})), JQ, JS, ML), zQ, vO.d8.apply(null, [EQ, Wk, MF]), mQ, vO.z8(UL(UL({})), TQ, DF, lc), vn]))

// "11272360|-1|5,1,34,242,274"


function LmO(a, b) {
    return Math.round(Math.random() * (b - a) + a);
}

function vH(a, b) {
    return a > b;
}

function Cc(a, b) {
    return a < b;
}

function array_53() {
    var T8O = function f8O() {
        var h8O = -1;
        var G8O = [(LmO(1, 5)).toString(), '1', (LmO(20, 70)).toString(), (LmO(100, 300)).toString(), (LmO(100, 300)).toString()];
        return [h8O, G8O];
    }();
    var W8O = T8O[1];
    var N8O = 1;
    if (vH(W8O.length, 0))
        for (var r8O = 0; Cc(r8O, W8O.length); r8O++) {
            var x8O = parseInt(W8O[r8O], 10);
            x8O && vH(x8O, 0) && (N8O *= x8O);
        }
    return [N8O, T8O[0], W8O].join('|');
}

console.log(YQ());
