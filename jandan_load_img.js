function jandan_load_img(b) {
    // 传入一个参数b，把b赋值给变量d，把d的img-hash赋值给f，把f的文本提取出来。。。说白了就是e等于图片的hash值
    var d = $(b);
    var f = d.next("span.img-hash");
    var e = f.text();
    f.remove();
    // 重点关注下面两句
    var c = jdN1vojzUDgDM5WyoSjf4YBLbPRYr4ovPc(e, "9e03YzcYoHuEBMj5eS4c2tbLVWiqSgn1");
    var a = $('<a href="' + c.replace(/(\/\/\w+\.sinaimg\.cn\/)(\w+)(\/.+\.(gif|jpg|jpeg))/, "$1large$3") + '" target="_blank" class="view_img_link">[查看原图]</a>');
    d.before(a);
    d.before("<br>");
    d.removeAttr("onload");
    d.attr("src", location.protocol + c.replace(/(\/\/\w+\.sinaimg\.cn\/)(\w+)(\/.+\.gif)/, "$1thumb180$3"));
    if (/\.gif$/.test(c)) {
        d.attr("org_src", location.protocol + c);
        b.onload = function() {
            add_img_loading_mask(this, load_sina_gif)
        }
    }
}