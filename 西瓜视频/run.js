!function(e) {
    function t(t) {
        for (var n, i, c = t[0], f = t[1], l = t[2], d = t[3] || [], p = 0, b = []; p < c.length; p++)
            i = c[p],
            Object.prototype.hasOwnProperty.call(o, i) && o[i] && b.push(o[i][0]),
            o[i] = 0;
        for (n in f)
            Object.prototype.hasOwnProperty.call(f, n) && (e[n] = f[n]);
        for (s && s(t),
        u.push.apply(u, d); b.length; )
            b.shift()();
        return a.push.apply(a, l || []),
        r()
    }
    function r() {
        for (var e, t = 0; t < a.length; t++) {
            for (var r = a[t], n = !0, f = 1; f < r.length; f++) {
                var l = r[f];
                0 !== o[l] && (n = !1)
            }
            n && (a.splice(t--, 1),
            e = c(c.s = r[0]))
        }
        return 0 === a.length && (u.forEach((function(e) {
            if (void 0 === o[e]) {
                o[e] = null;
                var t = document.createElement("link");
                c.nc && t.setAttribute("nonce", c.nc),
                t.rel = "prefetch",
                t.as = "script",
                t.href = i(e),
                document.head.appendChild(t)
            }
        }
        )),
        u.length = 0),
        e
    }
    var n = {}
      , o = {11: 0}
      , a = []
      , u = [];
    function i(e) {
        return c.p + "static/js/" + ({
            0: "vendors_@byted-ucenter/ttwid_flvjs",
            1: "@byted-growth/byte-sso-login-sdk-tob",
            2: "@byted-growth/web-certification",
            3: "@byted-ucenter/ttwid",
            4: "@byted/danmu-mask",
            5: "@fe/byted-search-debug-sdk",
            6: "flvjs",
            8: "loadPlayer",
            9: "lottie-web",
            10: "qrcode"
        }[e] || e) + "." + {
            0: "77aebf4d86",
            1: "f5017af87d",
            2: "7e0695adae",
            3: "051b03ff07",
            4: "7af5064913",
            5: "77df69c96d",
            6: "9d346c7d53",
            8: "efc1b4f168",
            9: "261a158283",
            10: "48ae43d19b"
        }[e] + ".chunk.js"
    }
    function c(t) {
        if (n[t])
            return n[t].exports;
        var r = n[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(r.exports, r, r.exports, c),
        r.l = !0,
        r.exports
    }
    c.e = function(e) {
        var t = []
          , r = o[e];
        if (0 !== r)
            if (r)
                t.push(r[2]);
            else {
                var n = new Promise((function(t, n) {
                    r = o[e] = [t, n]
                }
                ));
                t.push(r[2] = n);
                var a, u = document.createElement("script");
                u.charset = "utf-8",
                u.timeout = 120,
                c.nc && u.setAttribute("nonce", c.nc),
                u.src = i(e);
                var f = new Error;
                a = function(t) {
                    u.onerror = u.onload = null,
                    clearTimeout(l);
                    var r = o[e];
                    if (0 !== r) {
                        if (r) {
                            var n = t && ("load" === t.type ? "missing" : t.type)
                              , a = t && t.target && t.target.src;
                            f.message = "Loading chunk " + e + " failed.\n(" + n + ": " + a + ")",
                            f.name = "ChunkLoadError",
                            f.type = n,
                            f.request = a,
                            r[1](f)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    a({
                        type: "timeout",
                        target: u
                    })
                }
                ), 12e4);
                u.onerror = u.onload = a,
                document.head.appendChild(u)
            }
        return Promise.all(t)
    }
    ,
    c.m = e,
    c.c = n,
    c.d = function(e, t, r) {
        c.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: r
        })
    }
    ,
    c.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    c.t = function(e, t) {
        if (1 & t && (e = c(e)),
        8 & t)
            return e;
        if (4 & t && "object" === typeof e && e && e.__esModule)
            return e;
        var r = Object.create(null);
        if (c.r(r),
        Object.defineProperty(r, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var n in e)
                c.d(r, n, function(t) {
                    return e[t]
                }
                .bind(null, n));
        return r
    }
    ,
    c.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return c.d(t, "a", t),
        t
    }
    ,
    c.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    c.p = "https://sf6-scmcdn-tos.pstatp.com/obj/goofy/xigua_fe/xigua_video_web_pc/",
    c.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    var f = window.webpackJsonp = window.webpackJsonp || []
      , l = f.push.bind(f);
    f.push = t,
    f = f.slice();
    for (var d = 0; d < f.length; d++)
        t(f[d]);
    var s = l;
    r()
}([]);
//# sourceMappingURL=https://sourcemap-ixigua.com/obj/xigua-video-web-pc-sourcemap/xgpc/sourcemap/js/runtime_index.c6a213b498.js.map
