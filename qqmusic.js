t = {
    accepts: {script: 'text/javascript, application/javascript, application/x-javascript', json: 'application/json', xml: 'application/xml, text/xml', html: 'text/html', text: 'text/plain'},
    beforeSend: null,
    cache: false,
    complete: null,
    crossDomain: true,
    data: "{\"comm\":{\"cv\":4747474,\"ct\":24,\"format\":\"json\",\"inCharset\":\"utf-8\",\"outCharset\":\"utf-8\",\"notice\":0,\"platform\":\"yqq.json\",\"needNewCode\":1,\"uin\":1799413190,\"g_tk_new_20200303\":570667754,\"g_tk\":570667754},\"req_1\":{\"module\":\"music.globalComment.CommentRead\",\"method\":\"GetNewCommentList\",\"param\":{\"BizType\":4,\"BizId\":\"26\",\"LastCommentSeqNo\":\"\",\"PageSize\":25,\"PageNum\":0,\"FromCommentId\":\"\",\"WithHot\":1,\"PicEnable\":1,\"LastTotal\":0,\"LastTotalVer\":\"0\"}},\"req_2\":{\"module\":\"music.globalComment.CommentRead\",\"method\":\"GetHotCommentList\",\"param\":{\"BizType\":4,\"BizId\":\"26\",\"LastCommentSeqNo\":\"\",\"PageSize\":15,\"PageNum\":0,\"HotType\":2,\"WithAirborne\":1,\"PicEnable\":1}},\"req_3\":{\"module\":\"yqq.WhiteListServer\",\"method\":\"Pass\",\"param\":{}},\"req_4\":{\"module\":\"userInfo.VipQueryServer\",\"method\":\"SRFVipQuery_V2\",\"param\":{\"uin_list\":[\"1799413190\"]}},\"req_5\":{\"module\":\"userInfo.BaseUserInfoServer\",\"method\":\"get_user_baseinfo_v2\",\"param\":{\"vec_uin\":[\"1799413190\"]}},\"req_6\":{\"module\":\"MessageCenter.MessageCenterServer\",\"method\":\"GetMessage\",\"param\":{\"uin\":\"1799413190\",\"red_dot\":[{\"msg_type\":1}]}},\"req_7\":{\"module\":\"GlobalComment.GlobalCommentMessageReadServer\",\"method\":\"GetMessage\",\"param\":{\"uin\":\"1799413190\",\"page_num\":0,\"page_size\":1,\"last_msg_id\":\"\",\"type\":0}}}",
    dataType: "json",
    error: null,
    needSign: true,
    postType: true,
    success: null,
    time: 10000,
    type: "POST",
    url: "//u.y.qq.com/cgi-bin/musics.fcg?_=1660824376890",
    withCredentials: true
}
e= {
    "data": {
        "comm": {
            "cv": 4747474,
            "ct": 24,
            "format": "json",
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "platform": "yqq.json",
            "needNewCode": 1,
            "uin": 1799413190,
            "g_tk_new_20200303": 570667754,
            "g_tk": 570667754
        },
        "req_1": {
            "module": "music.globalComment.CommentRead",
            "method": "GetNewCommentList",
            "param": {
                "BizType": 4,
                "BizId": "26",
                "LastCommentSeqNo": "",
                "PageSize": 25,
                "PageNum": 0,
                "FromCommentId": "",
                "WithHot": 1,
                "PicEnable": 1,
                "LastTotal": 0,
                "LastTotalVer": "0"
            }
        },
        "req_2": {
            "module": "music.globalComment.CommentRead",
            "method": "GetHotCommentList",
            "param": {
                "BizType": 4,
                "BizId": "26",
                "LastCommentSeqNo": "",
                "PageSize": 15,
                "PageNum": 0,
                "HotType": 2,
                "WithAirborne": 1,
                "PicEnable": 1
            }
        },
        "req_3": {
            "module": "yqq.WhiteListServer",
            "method": "Pass",
            "param": {}
        },
        "req_4": {
            "module": "userInfo.VipQueryServer",
            "method": "SRFVipQuery_V2",
            "param": {
                "uin_list": [
                    "1799413190"
                ]
            }
        },
        "req_5": {
            "module": "userInfo.BaseUserInfoServer",
            "method": "get_user_baseinfo_v2",
            "param": {
                "vec_uin": [
                    "1799413190"
                ]
            }
        },
        "req_6": {
            "module": "MessageCenter.MessageCenterServer",
            "method": "GetMessage",
            "param": {
                "uin": "1799413190",
                "red_dot": [
                    {
                        "msg_type": 1
                    }
                ]
            }
        },
        "req_7": {
            "module": "GlobalComment.GlobalCommentMessageReadServer",
            "method": "GetMessage",
            "param": {
                "uin": "1799413190",
                "page_num": 0,
                "page_size": 1,
                "last_msg_id": "",
                "type": 0
            }
        }
    },
    "time": 10000,
    "withCredentials": true,
    "cache": false,
    "url": "//u.y.qq.com/cgi-bin/musicu.fcg",
    "postType": true,
    "type": "POST",
    "needSign": true
}
function add() {
    var i, o = n(350).default;
    i = "GET" === t.type.toUpperCase() ? o(t.data.data) : o(t.data)
    return i
}

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

function e(t, n, r, i, o, a, u, l) {
    var c = !i;
    t = +t,
        n = n || [0],
        i = i || [[this], [{}]],
        o = o || {};
    var s, f = [], p = null;
    Function.prototype.bind || (s = [].slice,
            Function.prototype.bind = function (e) {
                if ("function" != typeof this)
                    throw new TypeError("bind101");
                var t = s.call(arguments, 1)
                    , n = t.length
                    , r = this
                    , i = function () {
                }
                    , o = function () {
                    return t.length = n,
                        t.push.apply(t, arguments),
                        r.apply(i.prototype.isPrototypeOf(this) ? this : e, t)
                };
                return this.prototype && (i.prototype = this.prototype),
                    o.prototype = new i,
                    o
            }
    );
    for (var d = [function () {
        i[i.length - 2] = i[i.length - 2] + i.pop()
    }
        , function () {
            for (var a = n[t++], u = [], l = n[t++], c = n[t++], s = [], f = 0; f < l; f++)
                u[n[t++]] = i[n[t++]];
            for (f = 0; f < c; f++)
                s[f] = n[t++];
            i.push((function t() {
                    var i = u.slice(0);
                    i[0] = [this],
                        i[1] = [arguments],
                        i[2] = [t];
                    for (var l = 0; l < s.length && l < arguments.length; l++)
                        0 < s[l] && (i[s[l]] = [arguments[l]]);
                    return e(a, n, r, i, o)
                }
            ))
        }
        , function () {
            i[i.length - 2] = i[i.length - 2] | i.pop()
        }
        , function () {
            i.push(i[n[t++]][0])
        }
        , function () {
            var e = n[t++]
                , r = i[i.length - 2 - e];
            i[i.length - 2 - e] = i.pop(),
                i.push(r)
        }
        , , function () {
            var e = n[t++]
                , r = e ? i.slice(-e) : [];
            i.length -= e,
                e = i.pop(),
                i.push(e[0][e[1]].apply(e[0], r))
        }
        , , , function () {
            var e = n[t++];
            i[i.length - 1] && (t = e)
        }
        , function () {
            var e = n[t++]
                , r = e ? i.slice(-e) : [];
            i.length -= e,
                r.unshift(null),
                i.push(function () {
                    return function (e, t, n) {
                        return new (Function.bind.apply(e, t))
                    }
                        .apply(null, arguments)
                }(i.pop(), r))
        }
        , function () {
            i[i.length - 2] = i[i.length - 2] - i.pop()
        }
        , function () {
            var e = i[i.length - 2];
            e[0][e[1]] = i[i.length - 1]
        }
        , , function () {
            var e = n[t++];
            i[e] = void 0 === i[e] ? [] : i[e]
        }
        , , function () {
            i.push(!i.pop())
        }
        , , , , function () {
            i.push([n[t++]])
        }
        , function () {
            i[i.length - 1] = r[i[i.length - 1]]
        }
        , , function () {
            i.push("")
        }
        , , function () {
            i[i.length - 2] = i[i.length - 2] << i.pop()
        }
        , , function () {
            var e = i.pop();
            i.push([i[i.pop()][0], e])
        }
        , function () {
            i.push(i[i.pop()[0]][0])
        }
        , , function () {
            i[i.length - 1] = n[t++]
        }
        , function () {
            i[i.length - 2] = i[i.length - 2] >> i.pop()
        }
        , , function () {
            i.push(!1)
        }
        , function () {
            i[i.length - 2] = i[i.length - 2] > i.pop()
        }
        , , function () {
            i[i.length - 2] = i[i.length - 2] ^ i.pop()
        }
        , function () {
            i.push([i.pop(), i.pop()].reverse())
        }
        , function () {
            i.pop()
        }
        , function () {
            i[i[i.length - 2][0]][0] = i[i.length - 1]
        }
        , , , , function () {
            i.push(i[i.length - 1])
        }
        , , function () {
            return !0
        }
        , function () {
            i.push([r, i.pop()])
        }
        , function () {
            var e = n[t++]
                , o = e ? i.slice(-e) : [];
            i.length -= e,
                i.push(i.pop().apply(r, o))
        }
        , function () {
            i[i.length - 2] = i[i.length - 2] >= i.pop()
        }
        , , , function () {
            i.length = n[t++]
        }
        , , function () {
            var e = i.pop()
                , t = i.pop();
            i.push([t[0][t[1]], e])
        }
        , , function () {
            i[i.length - 2] = i[i.length - 2] & i.pop()
        }
        , function () {
            t = n[t++]
        }
        , , function () {
            i[i.length - 1] += String.fromCharCode(n[t++])
        }
        , , , function () {
            i[i.length - 2] = i[i.length - 2] === i.pop()
        }
        , function () {
            i.push(void 0)
        }
        , function () {
            var e = i.pop();
            i.push(e[0][e[1]])
        }
        , , function () {
            i.push(!0)
        }
        , , function () {
            i[i.length - 2] = i[i.length - 2] * i.pop()
        }
        , function () {
            i.push(n[t++])
        }
        , function () {
            i.push(typeof i.pop())
        }
    ]; ;)
        try {
            for (var h = !1; !h;)
                h = d[n[t++]]();
            if (p)
                throw p;
            return c ? (i.pop(),
                i.slice(3 + e.v)) : i.pop()
        } catch (m) {
            var v = f.pop();
            if (void 0 === v)
                throw m;
            p = m,
                t = v[0],
                i.length = v[1],
            v[2] && (i[v[2]][0] = p)
        }
}

function t() {
    var i = u.slice(0);
    i[0] = [this],
        i[1] = [arguments],
        i[2] = [t];
    for (var l = 0; l < s.length && l < arguments.length; l++)
        0 < s[l] && (i[s[l]] = [arguments[l]]);
    return e(a, n, r, i, o)
}
