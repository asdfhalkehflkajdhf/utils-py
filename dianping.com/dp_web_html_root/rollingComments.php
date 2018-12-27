<?php

?>
<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	
	<meta name="renderer" content="webkit">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
	<link rel="stylesheet" href="js/layui/css/layui.css"  media="all">
	<script src="js/echarts.min.js"></script>
	<script src="js/layui/layui.js" charset="utf-8"></script>
	<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>

	<!-- 布局样式 --> 
	<?php

	?>
	
    <link rel="stylesheet" type="text/css" href="http://www.dpfile.com/app/pc-common/index.min.30301999a81455aaf8a16973b3b13888.css">
    <link rel="stylesheet" type="text/css" href="http:////s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/34ef06940f33834b839aa152c209a6b1.css">
    <link rel="stylesheet" type="text/css" href="http://www.dpfile.com/app/dpindex-new-static/static/review-list.min.15bbeba96010d3af058fd94e65094a3b.css" />
	<link rel="stylesheet" type="text/css" href="http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/c91d98607cad828ff2a553ea5c4cf1c7.css" /> 
	<link rel="stylesheet" href="http://www.dpfile.com/app/app-pc-main/static/main-shop.min.2ee6ae4a33441a8ebcf3fb36d7db4e54.css" type="text/css" /> 

	  <link rel="stylesheet" href="http://www.dpfile.com/concat/~mod~mbox~1.0.4~css~mbox.css,~mod~easy-login~0.4.41~css~account.css,~mod~easy-login~0.4.41~css~style.css,~mod~easy-login~0.4.39~css~account.css,~mod~easy-login~0.4.39~css~style.css,~mod~main-authbox~1.0.9~css~index.css,~mod~css-rating~1.0.2~css~index.css,~mod~app-main-shop-remove~0.0.16~css~index.css,~mod~app-main-shop-basicinfo-change~1.1.35~css~index.css" type="text/css" />   

</head>
<body>

	<!-- 卡片面板 -->
	<div style="padding: 20px; background-color: #F2F2F2;">
	
		<div class="layui-col-md12" >
		  <div class="layui-card">
			<!--<div class="layui-card-header">标题</div>-->
			<div class="layui-card-body">
				<!--标题信息-->
			  	<?php

				?>
				      <h1 class="shop-name"> 满恒记火锅</h1> 
      <div class="brief-info"> 
       <span title="五星商户" class="mid-rank-stars mid-str50"></span> 
       <span id="reviewCount" class="item"> 1
        <d class="zl-tvPf"></d>
        <d class="zl-TohQ"></d>
        <d class="zl-Jvp2"></d>
        <d class="zl-giSW"></d> 条评论 </span> 
       <div class="star-from-desc J-star-from-desc Hide">
        星级来自业内综合评估
        <i class="icon"></i>
       </div> 
       <span id="avgPriceTitle" class="item">人均: 
        <d class="zl-FhcV"></d>
        <d class="zl-TohQ"></d> 元</span> 
       <span id="comment_score"> <span class="item">口味: 
         <d class="zl-FhcV"></d>.
         <d class="zl-gc5M"></d> </span> <span class="item">环境: 
         <d class="zl-htaN"></d>.
         <d class="zl-Jvp2"></d> </span> <span class="item">服务: 
         <d class="zl-htaN"></d>.
         <d class="zl-htaN"></d> </span> </span> 
      </div> 
      <div class="expand-info address" itemprop="street-address"> 
       <span class="info-name">地址：</span> 
       <span class="item" itemprop="street-address" id="address"> 
        <e class="jl-SMQf"></e>
        <e class="jl-MeGl"></e>里
        <e class="jl-KiFX"></e>
        <e class="jl-1Xp6"></e>
        <e class="jl-md7e"></e>1
        <d class="zl-Jvp2"></d>
        <e class="jl-Q71j"></e>(
        <e class="jl-SMQf"></e>
        <e class="jl-MeGl"></e>里
        <e class="jl-KiFX"></e>
        <e class="jl-1Xp6"></e>
        <e class="jl-md7e"></e>与赵登禹
        <e class="jl-vFcQ"></e>
        <e class="jl-jxjI"></e>叉口
        <e class="jl-KiFX"></e>
        <e class="jl-GG4Z"></e>角) </span> 
      </div> 
      <p class="expand-info tel"> <span class="info-name">电话：</span> 
       <d class="zl-JTyc"></d>1
       <d class="zl-JTyc"></d>-
       <d class="zl-TohQ"></d>
       <d class="zl-TohQ"></d>
       <d class="zl-Cg3x"></d>1
       <d class="zl-tvPf"></d>1
       <d class="zl-htaN"></d>
       <d class="zl-htaN"></d> </p> 
				
			</div>
		  </div>
		</div>
	
		  <div id="showContent" class="layui-row layui-col-space15">
			<div class="layui-col-md6">
			  <div class="layui-card">
				<!-- <div class="layui-card-header">图表</div> -->
				<div class="layui-card-body">
						<!--评论占比环形图-->
						<div id="pieTable" style="width:100%; "></div>
						<!--差评周趋势-->
						<div id="barTable" style="width:100%; "></div>

					</div>
			  </div>
			</div>
			
			<div class="layui-col-md6">
			  <div class="layui-card">
				<div class="layui-card-header">评论</div>
				<div class="layui-card-body">
					<!--评论列表-->
					<div id="review-list" class="review-list" >
							<div class="reviews-items">
								<ul>
									<!--点评评论样例-->
									
									<?php

									?>
									
													<li>
							<a class="dper-photo-aside"
							   target="_blank"
							   rel="nofollow"
							   href="http://www.dianping.com/member/4270497"
							   data-user-id="4270497"
							   data-click-name="用户头像0"
							   data-click-title="图片"
							>
								<img src="https://p0.meituan.net/userheadpic/dd5b28765159d99781af6ea7e933110818645.jpg%4048w_48h_1e_1c_1l%7Cwatermark%3D0">
								<!--若是月度之星-->
							</a>
						<div class="main-review">
							<div class="dper-info">
									<a class="name"
									   target="_blank"
									   rel="nofollow"
									   title=""
									   href="http://www.dianping.com/member/4270497"
									   data-click-name="用户名0"
									   data-click-title="文字"
									>
									小妮儿_好运
									</a>
									<span class="user-rank-rst urr-rank60 rank"></span>
										<span class="vip"></span>
							</div>
							<div class="review-rank">
									<span class="sml-rank-stars sml-str50 star"></span>
									<span class="score">
														<span class="item">
															口味：非常好
														</span>
														<span class="item">
															环境：非常好
														</span>
														<span class="item">
															服务：非常好
														</span>
											<span class="item">人均：0元</span>
									</span>
							</div>
								<div class="review-truncated-words">
									早<span class="fo-FMYy"></span>来呀，<span class="fo-vl99"></span><span class="fo-vl99"></span><span class="fo-vl99"></span><span class="fo-vl99"></span>。<br /><br />工作日晚餐四<span class="fo-FMYy"></span>半左<span class="fo-uwg3"></span>妥妥不用排<span class="fo-TbEE"></span>。<br /><br />菜单好像更新过了。<br /><br />「牛<span class="fo-CIkt"></span>髓」<span class="fo-nzAQ"></span>人很喜欢。...
									<div class="more-words">
										<a href="javascript:;"
										   class="fold"
										   data-click-name="展开评论0"
										   data-click-title="文字"
										>
											展开评论<i class="icon"></i>
										</a>
									</div>
								</div>
							<div class="review-words Hide">
								早点<span class="fo-Dlah"></span>呀，<span class="fo-vl99"></span><span class="fo-vl99"></span><span class="fo-vl99"></span><span class="fo-vl99"></span>。<br /><br />工作日晚餐四点半左右妥妥<span class="fo-QnSn"></span>用排队。<br /><br />菜单<span class="fo-S2Zg"></span>像<span class="fo-Rvf6"></span><span class="fo-ut3p"></span>过<span class="fo-QpDo"></span>。<br /><br />「<span class="fo-m7Ik"></span>骨髓」个<span class="fo-eIqh"></span>很<span class="fo-PHSY"></span>欢。<br /><br />「<span class="fo-yeoA"></span>牌麻酱糖饼」红糖多得溢出<span class="fo-Dlah"></span>。<br /><br />「鲜切苏<span class="fo-UIQj"></span>特后腿肥瘦」尝<span class="fo-QpDo"></span>各种肉，还是鲜切肥瘦羊肉最<span class="fo-S2Zg"></span>吃。<br /><br />[环<span class="fo-nOsG"></span>]这次<span class="fo-KmrF"></span>一楼，比楼上<span class="fo-S2Zg"></span>点。<br /><br />[服务]<span class="fo-QnSn"></span><span class="fo-5UxY"></span>。
								<div class="less-words">
									<a href="javascript:;"
									   class="unfold"
									   data-click-name="收起评论0"
									   data-click-title="文字"
									>
										收起评论<i class="icon"></i>
									</a>
								</div>
							</div>
								<div class="review-pictures">
									<ul>
											<li class="item">
												<a href="/photos/1312057668"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/N-VmXXnXWVnmebm4hI7nPxJ5eifNsNmOgEERQlIQVMHL9N8pnCEFRVF9xQoFasKpUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/N-VmXXnXWVnmebm4hI7nPxJ5eifNsNmOgEERQlIQVMFKoLK0EUv3isUhT-W-zYzZjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057670"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/oiFxUjR4KI_2MaoEmCDKDaGE2HheQOz_mvha_1Jwlszu_si0ySq6QVEo2JRia754UBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/oiFxUjR4KI_2MaoEmCDKDaGE2HheQOz_mvha_1Jwlsywm-6ysRu9PTKJV0SCKy_UjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057671"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/iFbCFF0CnLsyP9A_YYtr6s3416-I_c4xQTeu4FJhAqQ-_8kAMsX02uOwMSkcdYwyUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/iFbCFF0CnLsyP9A_YYtr6s3416-I_c4xQTeu4FJhAqSR-cGlPlGk8jbX_vnKR2oNjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057673"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/KpQub-3609kKCKvOnl1LW56rPkqfNl0lxN_4oT87U4L2zzn6c_ObByQugGhLmf9JUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/KpQub-3609kKCKvOnl1LW56rPkqfNl0lxN_4oT87U4KxACO8hNECLUNaAICf4EAKjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057674"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/yyz7h4q5fOieYtHxrg9np2dK8U_ZqjwMrM-EuCsv8C1hPX8L7L7G3enlmN8kFrVkUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/yyz7h4q5fOieYtHxrg9np2dK8U_ZqjwMrM-EuCsv8C0pJ36aly4bqURKSnWlKZwijoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057676"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/4t4kW31O4m-M-5rVUeyx1JV30o4ImH1a5LXs6WvrIoVrzenyg7XGE-YnuvGKtoHcUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/4t4kW31O4m-M-5rVUeyx1JV30o4ImH1a5LXs6WvrIoVCUbge5HlxwvWKA3naZwMDjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057677"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/V7dXWOuZTxX7YISnYRdYYQNcPmSnGXVTo99iI9E5KFACBeipjeh0JyjSN2MINoPDUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/V7dXWOuZTxX7YISnYRdYYQNcPmSnGXVTo99iI9E5KFCx0FB5XAwjlC-OyK5Y2SgajoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057678"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/4Drt7qjrRjRcFOY08aoRjvgNo8D6AfIbgdWDYRLI1DcGGSiJLHtLOaNanXz6fZFaUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/4Drt7qjrRjRcFOY08aoRjvgNo8D6AfIbgdWDYRLI1DdbcqjC2hLD4be2MxwQvOApjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057679"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/Wr6CjquJ7L8A1qiBiSE-b1SAr-CM0ve8HaszBkyeTJx9U7z6xMEPgE6g1VVohaOUUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/Wr6CjquJ7L8A1qiBiSE-b1SAr-CM0ve8HaszBkyeTJx6n5ZukaDKXbUZoWU-KbOFjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057681"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/_tOGs9vYdcI-TGyp36YaZ3xidTZ3riqiE8HzUlrkFEXumzmbwVOu_Ni9i-0iHty6UBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/_tOGs9vYdcI-TGyp36YaZ3xidTZ3riqiE8HzUlrkFEXJ-JMpgRkYwbGCsposq-WMjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057682"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/O47j4VrkRjriSn1TwzPI5fVAGtwCtLEyYoDDHjJgqVP4kIiR9-ulIwgxnBeKlRecUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/O47j4VrkRjriSn1TwzPI5fVAGtwCtLEyYoDDHjJgqVPjfRmSOycLFgUWB3SdU3RWjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
											<li class="item">
												<a href="/photos/1312057685"
												   data-click-name="评论图片0-"
												   data-click-title="文字"
												>
													<img src="http://qcloud.dpfile.com/pc/gGGiIuoT-B_SmWwpTgMEPC4e_AK4m42tQHJ2gI9eqKsksjL4B6KO3rbJj8lFNVeIUBBCaBtJvKU_sxCtKYAYUQ.jpg"
														 data-big="http://qcloud.dpfile.com/pc/gGGiIuoT-B_SmWwpTgMEPC4e_AK4m42tQHJ2gI9eqKvzCMCna6jGO3QFP0TdbirPjoJrvItByyS4HHaWdXyO_DrXIaWutJls2xCVbatkhjUNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"
													>
												</a>
											</li>
									</ul>
								</div>
							<div class="misc-info clearfix">
								<span class="time">
	2018-11-19 13:33                            
								</span>
									<span class="shop">满恒记火锅</span>
									<span class="actions">
										<!--若是本人点评-->
											<a href="javascript:;"
											   class="praise"
											   data-id="475921710"
											   rel="nofollow"
											   data-click-name="赞0"
											   data-click-title="文字"
											   data-send=""
											>
												赞
											</a>
												<em class="col-exp">(6)</em>
											<a href="//www.dianping.com/review/475921710"
											   target="_blank"
											   class="reply"
											   data-id="475921710"
											   data-click-name="回应0"
											   data-click-title="文字"
											>回应</a>
											<a href="javascript:;"
											   class="favor"
											   data-id="475921710"
											   rel="nofollow"
											   data-click-name="收藏0"
											   data-click-title="文字"
											>收藏</a>
											<a href="javascript:;"
											   class="report"
											   data-id="475921710"
											   dr-referuserid="2"
											   rel="nofollow"
											   data-click-name="投诉0"
											   data-click-title="文字"
											>投诉</a>
									</span>
							</div>
						</div>
					</li>
								</ul>
							</div>
					</div>

				</div>
			  </div>
			</div>
			
		  </div>
	</div> 


	<div >
</div>
<script>
$('.fold').click(function(){
	console.log(1);
	//　展开评论　先隐藏当前，再展开
	$(this).parent().parent().addClass("Hide");
	$(this).parent().parent().next().removeClass("Hide");
});
$('.unfold').click(function(){
	console.log(2);
	//　收起评论　先隐藏当前，再展开
	$(this).parent().parent().addClass("Hide");
	$(this).parent().parent().prev().removeClass("Hide");
	
});

</script>

<script type="text/javascript">


</script>
<script type="text/javascript">
// 获取高度
// https://www.cnblogs.com/whb17bcdq/p/6513766.html
	//初始化　echars 
	var pieTableObj = document.getElementById("pieTable")
	pieTableObj.style.height= window.screen.availHeight/2*0.7 +"px";
	pieTableObj.style.width = window.screen.availWidth/2*0.9+"px";

	console.log(window.screen.availHeight);
	console.log(pieTableObj);
	var g_pieChart = echarts.init(document.getElementById('pieTable'));
	
	//获取原始数据
	function getJsonValue(url){
	// https://blog.csdn.net/qq_28817739/article/details/79318667
		<!-- var res=$.Deferred(); -->
		var res=null;
		$.ajax({
			type:"get",
			url: url,
			data: {},//数据，这里使用的是Json格式进行传输 
			dataType: "json",
			async: false, 			// 特别注意，同步请求将锁住浏览器，用户其它操作必须等待请求完成才可以执行。
			success: function(data){
				res = data;
				<!-- res.resolve(data);  -->
			},
			error: function(data){
				console.log("get error:"+url);
			}
		});
		<!-- console.log(res); -->
		<!-- return res.promise(); -->
		return res;
	}

	// var g_nodes = getJsonValue("res/sampleGraphNodes.json");
	// var g_edges = getJsonValue("res/sampleGraphEdges.json");
	// var g_categories = getJsonValue("res/sampleGraphCategorys.json");
	// var g_levelEdges = getJsonValue("res/sampleGraphEdgesLevel.json");


// '嵌套环形图';

var pieOption = {
	title: {
		text: "",
		textStyle: {align: 'center'}
		
	},
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        data:['好评','中评','差评','好评5星','好评4星','差评0星','差评1星','差评2星']
    },
    series: [
        {
            name:'占比大小',
            type:'pie',
            selectedMode: 'single',
            radius: [0, '30%'],

            label: {
                normal: {
                    position: 'inner'
                }
            },
            labelLine: {
                normal: {
                    show: false
                }
            },
            data:[
                {value:335, name:'好评'},
                {value:679, name:'中评'},
                {value:1548, name:'差评', selected:true}
            ]
        },
        {
            name:'占比大小',
            type:'pie',
            radius: ['40%', '55%'],
            label: {
                normal: {
                    formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                    backgroundColor: '#eee',
                    borderColor: '#aaa',
                    borderWidth: 1,
                    borderRadius: 4,
                    // shadowBlur:3,
                    // shadowOffsetX: 2,
                    // shadowOffsetY: 2,
                    // shadowColor: '#999',
                    // padding: [0, 7],
                    rich: {
                        a: {
                            color: '#999',
                            lineHeight: 22,
                            align: 'center'
                        },
                        // abg: {
                        //     backgroundColor: '#333',
                        //     width: '100%',
                        //     align: 'right',
                        //     height: 22,
                        //     borderRadius: [4, 4, 0, 0]
                        // },
                        hr: {
                            borderColor: '#aaa',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: '#eee',
                            backgroundColor: '#334455',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            },
            data:[
                {value:135, name:'好评5星'},
                {value:200, name:'好评4星'},
                {value:679, name:'中评'},
                {value:548, name:'差评0星'},
                {value:500, name:'差评1星'},
                {value:500, name:'差评2星'}
            ]
        }
    ]
};;
if (pieOption && typeof pieOption === "object") {
    g_pieChart.setOption(pieOption, true);
}
</script>

<script type="text/javascript">
	//初始化　echars 
	var barTableObj = document.getElementById("barTable")
	barTableObj.style.height= window.screen.availHeight/2*0.7 +"px";
	barTableObj.style.width = window.screen.availWidth/2*0.9+"px";
	var g_barChart = echarts.init(barTableObj);
	

	// var g_nodes = getJsonValue("res/sampleGraphNodes.json");
	// var g_edges = getJsonValue("res/sampleGraphEdges.json");
	// var g_categories = getJsonValue("res/sampleGraphCategorys.json");
	// var g_levelEdges = getJsonValue("res/sampleGraphEdgesLevel.json");


// '嵌套环形图';

var barOption = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data: [ '好评4星','好评5星', '中评','差评0星', '差评1星','差评2星'],
		selected: {
           '好评4星': false, '好评5星': false, '中评': false
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis:  {
        type: 'category',
        data: ['前四周','前三周','前两周','前一周','当前']
    },
    yAxis: {
        type: 'value'
    },
    series: [
	
         {
            name: '好评4星',
            type: 'bar',
            stack: '好评总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [320, 302, 301, 334, 390]
        },
        {
            name: '好评5星',
            type: 'bar',
            stack: '好评总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [320, 302, 301, 334, 390]
        },
       {
            name: '中评',
            type: 'bar',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [320, 302, 301, 334, 390]
        },
    
        {
            name: '差评0星',
            type: 'bar',
            stack: '差评总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [320, 302, 301, 334, 390]
        },
        {
            name: '差评1星',
            type: 'bar',
            stack: '差评总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [120, 132, 101, 134, 90]
        },
        {
            name: '差评2星',
            type: 'bar',
            stack: '差评总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [220, 182, 191, 234, 290]
        }
    ]
};;
if (barOption && typeof barOption === "object") {
    g_barChart.setOption(barOption, true);
}
</script>


</body>


