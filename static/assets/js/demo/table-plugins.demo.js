/*
Template Name: HUD - Responsive Bootstrap 5 Admin Template
Version: 1.8.0
Author: Sean Ngu

*/

var handleRenderWebQueryTableData = function (f) {

	let column_num = f.length;
	let data_num = f[0].length;

	var data = []
	var column = []
	var columnDef = []
	for (var i = 0; i < column_num; i++){
		var data_dict = {}
		for (var j = 0; j < data_num; j++){
			data_dict["data" + (j + 1)] = f[i][j];
		}
		data.push(data_dict);
	};

	for (var i = 0; i < data_num; i++){
		let column_dict = {};
		let columnDef_dict = {};
		column_dict['data'] = "data" + (i + 1);
		columnDef_dict["width"] = "100px";
		columnDef_dict["target"] = i ;
		column.push(column_dict);
		columnDef.push(columnDef_dict);
	};

	console.log(columnDef);
	var webQueryTable = $('#webQuery_table').DataTable({
		dom: `<'row'<'col-md-4 mb-3 mb-md-0'l><'col-md-8 text-right'<'d-flex justify-content-end '>>>t<'row align-items-center'<'mr-auto col-md-6 mb-3 mb-md-0 mt-n2 'i><'mb-0 col-md-6'p>>`,
		destroy: true,
		lengthMenu: [10, 20, 30, 40, 50],
		info: false,
		details: false,
		searching: false,
		autoWidth: false,
		ordering: false,
		scrollX: 300,
		scrollY: 300,
		scrollCollapse: true,
		paging: false,
		responsive: false,
		colReorder: {
            allowReorder: true,
		},
		data : data,
		columns: column,
		columnDefs: columnDef,
		language: {
			"decimal": "",
			"info": "현재 _START_ - _END_건 / 전체 _TOTAL_건",
			"infoEmpty": "데이터가 없습니다.",
			"emptyTable": "데이터가 없습니다.",
			"thousands": ",",
			"lengthMenu": "페이지당 _MENU_ 개씩 보기",
			"loadingRecords": "로딩 중입니다.",
			"processing": "",
			"zeroRecords": "검색 결과 없음",
			"paginate": {
				"first": "처음",
				"last": "끝",
				"next": "다음",
				"previous": "이전"
			},
			"search": "검색:",
			"infoFiltered": "(전체 _MAX_ 건 중 검색결과)",
			"infoPostFix": "",
		},
	});

	return webQueryTable;
};

var handleRenderpropertiesTableData = function () {
	var propertiesTable = $('#properties_Table').DataTable({
	    dom: "<>t",
		responsive: false,
		destroy : true,
		searching: false,
		autoWidth: false,
		info: false,
		ordering: false,
		paging: false,
		scrollY: '750px',
		scrollX: true,
		scrollCollapse: true,
		colReorder: {
		          allowReorder: true
		          },
	});
};

var handleRenderQueryHistoryTableData = function () {
	var QueryHistoryTable = $('#queryHistoryTable').DataTable({
		dom: "<'row'<'col-md-4 mb-3 mb-md-0'l><'col-md-8 text-right'<'d-flex justify-content-end 'fB>>>t<'row align-items-center'<'mr-auto col-md-6 mb-3 mb-md-0 mt-n2 'i><'mb-0 col-md-6'p>>",
		lengthMenu: [10, 20, 30, 40, 50],
        scrollY: 240,
        scrollX: true,
        scrollCollapse: true,
        responsive: false,
		destroy : true,
		details: false,
		searching: false,
		autoWidth: false,
		info: false,
		ordering: false,
		paging: false,
		colReorder: {
		    allowReorder: true,
		},
		columnDefs: [
            { width: "4%", target: [0]},
            { width: "10%", target: [1] },
            { width: "6%", target: [2] },
            { width: "6%", target: [3] },
            { width: "6%", target: [4] },
            { width: "6%", target: [5] },
            { width: "41%", target: [6], className: 'text-start'},
            { width: "21%", target: [7], className: 'text-start'}
		],
		language: {
			"decimal": "",
			"info": "현재 _START_ - _END_건 / 전체 _TOTAL_건",
			"infoEmpty": "데이터가 없습니다.",
			"emptyTable": "데이터가 없습니다.",
			"thousands": ",",
			"lengthMenu": "페이지당 _MENU_ 개씩 보기",
			"loadingRecords": "로딩 중입니다.",
			"processing": "",
			"zeroRecords": "검색 결과 없음",
			"paginate": {
				"first": "처음",
				"last": "끝",
				"next": "다음",
				"previous": "이전"
			},
			"search": "검색:",
			"infoFiltered": "(전체 _MAX_ 건 중 검색결과)",
			"infoPostFix": "",
		},
	});
};

var handleRenderDbConnectedTableData = function () {
	var DbConnectedTable = $('#DbConnectedTable').DataTable({
		dom: "<'row'<'col-md-4 mb-3 mb-md-0'l><'col-md-8 text-right'<'d-flex justify-content-end 'fB>>>t<'row align-items-center'<'mr-auto col-md-6 mb-3 mb-md-0 mt-n2 'i><'mb-0 col-md-6'p>>",
		lengthMenu: [10, 20, 30, 40, 50],
        scrollY: 380,
        scrollX: true,
        scrollCollapse: true,
        responsive: false,
		destroy : true,
		details: false,
		searching: false,
		autoWidth: false,
		info: false,
		ordering: false,
		paging: false,
		colReorder: {
		    allowReorder: true,
		},
		/*columnDefs: [
            { width: "2%", target: [0] },
            { width: "4%", target: [1] },
            { width: "20%", target: [2] },
            { width: "66%", target: [3] },
            { width: "3%", target: [4] },
            { width: "4%", target: [5] }
		],*/
		language: {
			"decimal": "",
			"info": "현재 _START_ - _END_건 / 전체 _TOTAL_건",
			"infoEmpty": "데이터가 없습니다.",
			"emptyTable": "데이터가 없습니다.",
			"thousands": ",",
			"lengthMenu": "페이지당 _MENU_ 개씩 보기",
			"loadingRecords": "로딩 중입니다.",
			"processing": "",
			"zeroRecords": "검색 결과 없음",
			"paginate": {
				"first": "처음",
				"last": "끝",
				"next": "다음",
				"previous": "이전"
			},
			"search": "검색:",
			"infoFiltered": "(전체 _MAX_ 건 중 검색결과)",
			"infoPostFix": "",
		},
	});
};

/* Controller weakBoxs
------------------------------------------------ */
$(document).ready(function () {
	/*if($("#webQuery_table").length > 0){
	    handleRenderWebQueryTableData();
	}else if($("#properties_Table").length > 0){
	    handleRenderpropertiesTableData();
	}else */if($("#queryHistoryTable").length > 0){
	    handleRenderQueryHistoryTableData();
	}else if($("#DbConnectedTable").length > 0){
	    handleRenderDbConnectedTableData();
	};
});
