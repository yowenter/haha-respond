webpackJsonp([1],{0:function(e,n){},FGhX:function(e,n,t){e.exports=t.p+"dashboard/static/img/bg.24faefa.gif"},ID02:function(e,n){},L4ez:function(e,n){},NHnr:function(e,n,t){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var o=t("7+uW"),c={render:function(){var e=this.$createElement,n=this._self._c||e;return n("div",{attrs:{id:"app"}},[n("router-view")],1)},staticRenderFns:[]};var s=t("VU/8")({name:"App"},c,!1,function(e){t("L4ez")},null,null).exports,i=t("/ocq"),a=t("DmT9"),r=t.n(a),u=t("mtWM"),m=t.n(u),A="http://haha-static.daocom.io";Object({NODE_ENV:"production"}).API_URL&&(A=Object({NODE_ENV:"production"}).API_URL,"/"===Object({NODE_ENV:"production"}).API_URL&&(A=".")),o.a.prototype.API_URL=A;m.a.create({baseURL:A,headers:{"Content-Type":"application/json"}});var f=A,g=new o.a,l="."===f?"":f,d=void 0;d&&d.disconnect(),(d=r()(""+l,{path:"/danmus/socket.io"})).on("connect",function(){d.emit("enter_room","88888"),console.log("enter_comment_room")}),d.on("comment",function(e){console.log("comment",e),g.$emit("comment",e)}),d.on("disconnect",function(){console.log("comment_disconnect")});var C=t("FGhX"),p=t.n(C),h=t("jWhC"),B=t.n(h),Q={name:"Comment",props:["data","index"],data:function(){return{clientWidth:0,clientHeight:0,divWidth:0,divHeight:0,startTime:0,speed:100,transStyle:"",roby:"roby.chen@daocloud.io"}},mounted:function(){this.startTime=+new Date,this.divWidth=parseInt(window.getComputedStyle(this.$refs.comment).width,10)+50,this.divHeight=Math.floor(Math.random()*this.clientHeight)},created:function(){this.clientWidth=parseInt(document.body.clientWidth,10),this.clientHeight=parseInt(document.body.clientHeight,10)-200,requestAnimationFrame(this.setTransStyle)},methods:{setTransStyle:function(){var e=(+new Date-this.startTime)/1e3,n=this.clientWidth-this.speed*e;this.transStyle="transform: translate3d("+n+"px, "+this.divHeight+"px, 0)",n>-this.divWidth?requestAnimationFrame(this.setTransStyle):this.$emit("end",this.data)},isRoby:function(e){return e.email===this.roby}}},E={render:function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{ref:"comment",class:{comment:!0,gold:e.isRoby(e.data)},style:e.transStyle},[t("span",{staticClass:"user"},[e._v(e._s(e.data.user))]),e._v(" "),t("span",{staticClass:"message"},[e._v(e._s(e.data.message))])])},staticRenderFns:[]};var v={name:"Comments",components:{Comment:t("VU/8")(Q,E,!1,function(e){t("ID02")},null,null).exports},data:function(){return{comments:[]}},mounted:function(){var e=this;g.$on("comment",function(n){e.comments.push(n)})},methods:{destory:function(e){var n=0;this.comments.forEach(function(t,o){t.time===e.time&&t.message===e.message&&t.email===e.email&&(n=o)}),this.comments.splice(n,1)}}},X={render:function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{staticClass:"comments"},e._l(e.comments,function(n,o){return t("comment",{key:n.time,attrs:{data:n,index:o},on:{end:e.destory}})}))},staticRenderFns:[]};var y={name:"Index",components:{Comments:t("VU/8")(v,X,!1,function(e){t("bpGI")},null,null).exports},data:function(){return{bg:p.a,qrcode:B.a}}},L={render:function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{staticClass:"index"},[t("div",{staticClass:"bg-wrapper"},[t("img",{staticClass:"bg",attrs:{src:e.bg}})]),e._v(" "),t("div",{staticClass:"qrcode-wrapper"},[t("img",{staticClass:"qrcode",attrs:{src:e.qrcode}})]),e._v(" "),t("comments")],1)},staticRenderFns:[]};var P=t("VU/8")(y,L,!1,function(e){t("fpVc")},null,null).exports;o.a.use(i.a);var U=new i.a({routes:[{path:"/",name:"Index",component:P}]});o.a.config.productionTip=!1,new o.a({el:"#app",router:U,components:{App:s},template:"<App/>"})},bpGI:function(e,n){},fpVc:function(e,n){},jWhC:function(e,n){e.exports="data:image/png;base64,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"}},["NHnr"]);
//# sourceMappingURL=app.8a776f9c7bec71de648f.js.map