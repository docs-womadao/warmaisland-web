(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6c3e2d10"],{"565b":function(t,a,s){"use strict";s.r(a);var o=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",[t._m(0),s("div",{staticClass:"partd"},[s("center",[s("div",{staticClass:"download1"},[s("button",{attrs:{id:"myBtn"},on:{click:t.download_hook}},[s("div",[t._v("下载客户端")])]),s("el-dialog",{attrs:{title:"下载",visible:t.download,width:"30%","before-close":t.handleClose}},[s("span",{staticClass:"flexcenter"},[s("span",[t._v(t._s(t.downloadtext))])]),t.infoshow?s("span",[t._v("还未开始下载？"),s("a",{on:{click:t.download}},[t._v("开始下载")])]):t._e()])],1)])],1)])},e=[function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"maintext",staticStyle:{height:"100%"}},[s("p",{staticClass:"title1"},[t._v(" 沃玛岛PCL客户端 ")]),s("p",{staticClass:"title2"},[t._v(" 需要"),s("a",{staticClass:"blink",attrs:{href:"https://www.microsoft.com/en-us/download/details.aspx?id=42642",title:"下载 .NET Framework 4.5.2"}},[t._v(".Net Framework 4.5.2")]),t._v("运行环境 ")]),s("p",{staticClass:"title2"},[t._v(" 需要"),s("b",[t._v("WINDOWS 7")]),t._v("及以上操作系统 ")]),s("p",{staticClass:"title2"},[t._v(" 需要"),s("a",{staticClass:"blink",attrs:{href:"https://www.java.com/zh-CN/",title:"下载最新版JAVA"}},[t._v("JAVA8")]),t._v("及以上JAVA环境 ")])])}],i={data:function(){return{rootclass:"download-pc in-pc",addclass:"",downloadtext:"正在检查设备环境...",infoshow:!1,download:!1}},methods:{download:function(){this.$hardware.download("https://wmdclientdownload.warma.ren","WarmaIslandInstaller-v2.rar")},checkdevice:function(){},download_hook:function(){var t=this;this.download=!0,this.$hardware.checkphone()?(this.rootclass="is-mobile",this.downloadtext="推荐进入基岩版服务器，请自行查询基岩版Minecraft服务器进入教程"):(this.addclass="pc",this.$hardware.ismac()?this.downloadtext="Mac 客户端没有发布，请自行加入服务器":64==this.$hardware.getprocessors()?(this.downloadtext="正在下载沃玛岛整合包Windows版",this.$hardware.download("https://api.womadao.top:8000/client.rar","WarmaIslandInstaller-v2.rar"),setTimeout((function(){t.infoshow=!0}),3e3)):this.downloadtext="处理器版本过低，请升级到64位系统")},handleClose:function(t){this.download=!1,t()}},created:function(){}},n=i,d=(s("6da7"),s("2877")),l=Object(d["a"])(n,o,e,!1,null,"146318ed",null);a["default"]=l.exports},"6a59":function(t,a,s){},"6da7":function(t,a,s){"use strict";s("6a59")}}]);