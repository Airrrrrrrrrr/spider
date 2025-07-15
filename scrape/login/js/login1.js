window = this;
;;;(function(e) {
    function t(t) {
        for (var r, o, u = t[0], i = t[1], s = t[2], l = 0, f = []; l < u.length; l++)
            o = u[l],
            Object.prototype.hasOwnProperty.call(a, o) && a[o] && f.push(a[o][0]),
            a[o] = 0;
        for (r in i)
            Object.prototype.hasOwnProperty.call(i, r) && (e[r] = i[r]);
        d && d(t);
        while (f.length)
            f.shift()();
        return c.push.apply(c, s || []),
        n()
    }
    function n() {
        for (var e, t = 0; t < c.length; t++) {
            for (var n = c[t], r = !0, o = 1; o < n.length; o++) {
                var u = n[o];
                0 !== a[u] && (r = !1)
            }
            r && (c.splice(t--, 1),
            e = i(i.s = n[0]))
        }
        return e
    }
    var r = {}
      , o = {
        app: 0
    }
      , a = {
        app: 0
    }
      , c = [];
    function u(e) {
        return i.p + "js/" + ({}[e] || e) + "." + {
            "chunk-cc71364c": "d38f911d"
        }[e] + ".js"
    }
    function i(t) {
        if (r[t])
            return r[t].exports;
        var n = r[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        window.code += "\"" + t + "\":" + e[t] + ",";
		return e[t].call(n.exports, n, n.exports, i),
        n.l = !0,
        n.exports
    }
	window.jsy = i;
    i.e = function(e) {
        var t = []
          , n = {
            "chunk-cc71364c": 1
        };
        o[e] ? t.push(o[e]) : 0 !== o[e] && n[e] && t.push(o[e] = new Promise((function(t, n) {
            for (var r = "css/" + ({}[e] || e) + "." + {
                "chunk-cc71364c": "ac589904"
            }[e] + ".css", a = i.p + r, c = document.getElementsByTagName("link"), u = 0; u < c.length; u++) {
                var s = c[u]
                  , l = s.getAttribute("data-href") || s.getAttribute("href");
                if ("stylesheet" === s.rel && (l === r || l === a))
                    return t()
            }
            var f = document.getElementsByTagName("style");
            for (u = 0; u < f.length; u++) {
                s = f[u],
                l = s.getAttribute("data-href");
                if (l === r || l === a)
                    return t()
            }
            var d = document.createElement("link");
            d.rel = "stylesheet",
            d.type = "text/css",
            d.onload = t,
            d.onerror = function(t) {
                var r = t && t.target && t.target.src || a
                  , c = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                c.code = "CSS_CHUNK_LOAD_FAILED",
                c.request = r,
                delete o[e],
                d.parentNode.removeChild(d),
                n(c)
            }
            ,
            d.href = a;
            var p = document.getElementsByTagName("head")[0];
            p.appendChild(d)
        }
        )).then((function() {
            o[e] = 0
        }
        )));
        var r = a[e];
        if (0 !== r)
            if (r)
                t.push(r[2]);
            else {
                var c = new Promise((function(t, n) {
                    r = a[e] = [t, n]
                }
                ));
                t.push(r[2] = c);
                var s, l = document.createElement("script");
                l.charset = "utf-8",
                l.timeout = 120,
                i.nc && l.setAttribute("nonce", i.nc),
                l.src = u(e);
                var f = new Error;
                s = function(t) {
                    l.onerror = l.onload = null,
                    clearTimeout(d);
                    var n = a[e];
                    if (0 !== n) {
                        if (n) {
                            var r = t && ("load" === t.type ? "missing" : t.type)
                              , o = t && t.target && t.target.src;
                            f.message = "Loading chunk " + e + " failed.\n(" + r + ": " + o + ")",
                            f.name = "ChunkLoadError",
                            f.type = r,
                            f.request = o,
                            n[1](f)
                        }
                        a[e] = void 0
                    }
                }
                ;
                var d = setTimeout((function() {
                    s({
                        type: "timeout",
                        target: l
                    })
                }
                ), 12e4);
                l.onerror = l.onload = s,
                document.head.appendChild(l)
            }
        return Promise.all(t)
    }
    ,
    i.m = e,
    i.c = r,
    i.d = function(e, t, n) {
        i.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: n
        })
    }
    ,
    i.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    i.t = function(e, t) {
        if (1 & t && (e = i(e)),
        8 & t)
            return e;
        if (4 & t && "object" === typeof e && e && e.__esModule)
            return e;
        var n = Object.create(null);
        if (i.r(n),
        Object.defineProperty(n, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var r in e)
                i.d(n, r, function(t) {
                    return e[t]
                }
                .bind(null, r));
        return n
    }
    ,
    i.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e["default"]
        }
        : function() {
            return e
        }
        ;
        return i.d(t, "a", t),
        t
    }
    ,
    i.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    i.p = "/",
    i.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    var s = window["webpackJsonp"] = window["webpackJsonp"] || []
      , l = s.push.bind(s);
    s.push = t,
    s = s.slice();
    for (var f = 0; f < s.length; f++)
        t(s[f]);
    var d = l;
    //c.push([0, "chunk-vendors"]),
    //n()
}
)({"27ae":function(module, exports, __webpack_require__) {
        (function(global) {
            var __WEBPACK_AMD_DEFINE_ARRAY__, __WEBPACK_AMD_DEFINE_RESULT__;
            (function(e, r) {
                module.exports = r(e)
            }
            )("undefined" !== typeof self ? self : "undefined" !== typeof window ? window : "undefined" !== typeof global ? global : this, (function(global) {
                "use strict";
                global = global || {};
                var _Base64 = global.Base64, version = "2.5.1", buffer;
                if (module.exports)
                    try {
                        buffer = eval("require('buffer').Buffer")
                    } catch (err) {
                        buffer = void 0
                    }
                var b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                  , b64tab = function(e) {
                    for (var r = {}, o = 0, t = e.length; o < t; o++)
                        r[e.charAt(o)] = o;
                    return r
                }(b64chars)
                  , fromCharCode = String.fromCharCode
                  , cb_utob = function(e) {
                    if (e.length < 2) {
                        var r = e.charCodeAt(0);
                        return r < 128 ? e : r < 2048 ? fromCharCode(192 | r >>> 6) + fromCharCode(128 | 63 & r) : fromCharCode(224 | r >>> 12 & 15) + fromCharCode(128 | r >>> 6 & 63) + fromCharCode(128 | 63 & r)
                    }
                    r = 65536 + 1024 * (e.charCodeAt(0) - 55296) + (e.charCodeAt(1) - 56320);
                    return fromCharCode(240 | r >>> 18 & 7) + fromCharCode(128 | r >>> 12 & 63) + fromCharCode(128 | r >>> 6 & 63) + fromCharCode(128 | 63 & r)
                }
                  , re_utob = /[\uD800-\uDBFF][\uDC00-\uDFFFF]|[^\x00-\x7F]/g
                  , utob = function(e) {
                    return e.replace(re_utob, cb_utob)
                }
                  , cb_encode = function(e) {
                    var r = [0, 2, 1][e.length % 3]
                      , o = e.charCodeAt(0) << 16 | (e.length > 1 ? e.charCodeAt(1) : 0) << 8 | (e.length > 2 ? e.charCodeAt(2) : 0)
                      , t = [b64chars.charAt(o >>> 18), b64chars.charAt(o >>> 12 & 63), r >= 2 ? "=" : b64chars.charAt(o >>> 6 & 63), r >= 1 ? "=" : b64chars.charAt(63 & o)];
                    return t.join("")
                }
                  , btoa = global.btoa ? function(e) {
                    return global.btoa(e)
                }
                : function(e) {
                    return e.replace(/[\s\S]{1,3}/g, cb_encode)
                }
                  , _encode = buffer ? buffer.from && Uint8Array && buffer.from !== Uint8Array.from ? function(e) {
                    return (e.constructor === buffer.constructor ? e : buffer.from(e)).toString("base64")
                }
                : function(e) {
                    return (e.constructor === buffer.constructor ? e : new buffer(e)).toString("base64")
                }
                : function(e) {
                    return btoa(utob(e))
                }
                  , encode = function(e, r) {
                    return r ? _encode(String(e)).replace(/[+\/]/g, (function(e) {
                        return "+" == e ? "-" : "_"
                    }
                    )).replace(/=/g, "") : _encode(String(e))
                }
                  , encodeURI = function(e) {
                    return encode(e, !0)
                }
                  , re_btou = new RegExp(["[À-ß][-¿]", "[à-ï][-¿]{2}", "[ð-÷][-¿]{3}"].join("|"),"g")
                  , cb_btou = function(e) {
                    switch (e.length) {
                    case 4:
                        var r = (7 & e.charCodeAt(0)) << 18 | (63 & e.charCodeAt(1)) << 12 | (63 & e.charCodeAt(2)) << 6 | 63 & e.charCodeAt(3)
                          , o = r - 65536;
                        return fromCharCode(55296 + (o >>> 10)) + fromCharCode(56320 + (1023 & o));
                    case 3:
                        return fromCharCode((15 & e.charCodeAt(0)) << 12 | (63 & e.charCodeAt(1)) << 6 | 63 & e.charCodeAt(2));
                    default:
                        return fromCharCode((31 & e.charCodeAt(0)) << 6 | 63 & e.charCodeAt(1))
                    }
                }
                  , btou = function(e) {
                    return e.replace(re_btou, cb_btou)
                }
                  , cb_decode = function(e) {
                    var r = e.length
                      , o = r % 4
                      , t = (r > 0 ? b64tab[e.charAt(0)] << 18 : 0) | (r > 1 ? b64tab[e.charAt(1)] << 12 : 0) | (r > 2 ? b64tab[e.charAt(2)] << 6 : 0) | (r > 3 ? b64tab[e.charAt(3)] : 0)
                      , n = [fromCharCode(t >>> 16), fromCharCode(t >>> 8 & 255), fromCharCode(255 & t)];
                    return n.length -= [0, 0, 2, 1][o],
                    n.join("")
                }
                  , _atob = global.atob ? function(e) {
                    return global.atob(e)
                }
                : function(e) {
                    return e.replace(/\S{1,4}/g, cb_decode)
                }
                  , atob = function(e) {
                    return _atob(String(e).replace(/[^A-Za-z0-9\+\/]/g, ""))
                }
                  , _decode = buffer ? buffer.from && Uint8Array && buffer.from !== Uint8Array.from ? function(e) {
                    return (e.constructor === buffer.constructor ? e : buffer.from(e, "base64")).toString()
                }
                : function(e) {
                    return (e.constructor === buffer.constructor ? e : new buffer(e,"base64")).toString()
                }
                : function(e) {
                    return btou(_atob(e))
                }
                  , decode = function(e) {
                    return _decode(String(e).replace(/[-_]/g, (function(e) {
                        return "-" == e ? "+" : "/"
                    }
                    )).replace(/[^A-Za-z0-9\+\/]/g, ""))
                }
                  , noConflict = function() {
                    var e = global.Base64;
                    return global.Base64 = _Base64,
                    e
                };
                if (global.Base64 = {
                    VERSION: version,
                    atob: atob,
                    btoa: btoa,
                    fromBase64: decode,
                    toBase64: encode,
                    utob: utob,
                    encode: encode,
                    encodeURI: encodeURI,
                    btou: btou,
                    decode: decode,
                    noConflict: noConflict,
                    __buffer__: buffer
                },
                "function" === typeof Object.defineProperty) {
                    var noEnum = function(e) {
                        return {
                            value: e,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    };
                    global.Base64.extendString = function() {
                        Object.defineProperty(String.prototype, "fromBase64", noEnum((function() {
                            return decode(this)
                        }
                        ))),
                        Object.defineProperty(String.prototype, "toBase64", noEnum((function(e) {
                            return encode(this, e)
                        }
                        ))),
                        Object.defineProperty(String.prototype, "toBase64URI", noEnum((function() {
                            return encode(this, !0)
                        }
                        )))
                    }
                }
                return global["Meteor"] && (Base64 = global.Base64),
                module.exports ? module.exports.Base64 = global.Base64 : (__WEBPACK_AMD_DEFINE_ARRAY__ = [],
                __WEBPACK_AMD_DEFINE_RESULT__ = function() {
                    return global.Base64
                }
                .apply(exports, __WEBPACK_AMD_DEFINE_ARRAY__),
                void 0 === __WEBPACK_AMD_DEFINE_RESULT__ || (module.exports = __WEBPACK_AMD_DEFINE_RESULT__)),
                {
                    Base64: global.Base64
                }
            }
            ))
        }
        ).call(this, __webpack_require__("c8ba"))
    },"c8ba":function(e, t) {
        var n;
        n = function() {
            return this
        }();
        try {
            n = n || new Function("return this")()
        } catch (i) {
            "object" === typeof window && (n = window)
        }
        e.exports = n
    },
});

var c = window.jsy("27ae").Base64
var e = c.encode('{"username":"admin","password":"admin"}');