var game_list_table = "";

function init_list_table() {
    game_list_table = $("#gameListTable").DataTable(
        {
            "sPaginationType": "full_numbers",
            "iDisplayLength": 10,
            "bAutoWidth": false,
            "bLengthChange": false,
            "bFilter": false,
            "bProcessing": true,
            "oLanguage": {
                "sLengthMenu": "每页显示 _MENU_条",
                "sZeroRecords": "没有找到符合条件的数据",
                "sProcessing": "&lt;img src=’./loading.gif’ /&gt;",
                "sInfo": "当前第 _START_ - _END_ 条　共计 _TOTAL_ 条",
                "sInfoEmpty": "木有记录",
                "sInfoFiltered": "(从 _MAX_ 条记录中过滤)",
                "sSearch": "搜索：",
                "oPaginate": {
                    "sFirst": "首页",
                    "sPrevious": "前一页",
                    "sNext": "后一页",
                    "sLast": "尾页"
                }
            },
            "bServerSide": true,
            "sAjaxSource": "/record/list_json",
            "aoColumns": [
                {"data": 'name', "sWidth": "15%"},
                {"data": 'circle', "sWidth": "8%"},
                {"data": 'base', "sWidth": "8%"},
                {"data": "start_dt", "sWidth": "15%"},
                {"data": 'member1', "sWidth": "10%"},
                {"data": 'member2', "sWidth": "10%"},
                {"data": 'member3', "sWidth": "10%"},
                {"data": 'member4', "sWidth": "10%"}
            ],
            "columnDefs": [
                {
                    "targets": 0,
                    "data": "name",
                    "render": function (data, type, full) {
                        return '<a href="/record/' + full.id + '">' + data + '</a>';
                    }
                },
                {
                    "targets": 4,
                    "data": "name",
                    "render": function (data, type, full) {
                        return '<a href="#">' + full.member1 + '</a>: ' + full.score1;
                    }
                },
                {
                    "targets": 5,
                    "data": "name",
                    "render": function (data, type, full) {
                        return '<a href="#">' + full.member2 + '</a>: ' + full.score2;
                    }
                },
                {
                    "targets": 6,
                    "data": "name",
                    "render": function (data, type, full) {
                        return '<a href="#">' + full.member3 + '</a>: ' + full.score3;
                    }
                },
                {
                    "targets": 7,
                    "data": "name",
                    "render": function (data, type, full) {
                        return '<a href="#">' + full.member4 + '</a>: ' + full.score4;
                    }
                },
                {
                    "targets": 8,
                    "data": "name",
                    "render": function (data, type, full) {
                        var op_str = '<a href="javascript:void(0)">详情</a>&nbsp&nbsp|&nbsp&nbsp';
                        op_str += '<a href="/record/record/' + full.id + '">记分</a>&nbsp&nbsp|&nbsp&nbsp';
                        op_str += '<a href="javascript:void(0)" onclick="delete_game(' + full.id + ')">删除</a>';
                        return op_str;
                    }
                }
            ]
        }
    );
}

function delete_game(game_id) {
    $.ajax({
        type: "post",
        url: '/record/delete_game',
        dataType: 'json',
        data: {
            'game_id': game_id
        },
        success: function () {
            game_list_table.ajax.reload();
        },
        error: function () {
            game_list_table.ajax.reload();
        }
    });
}


$(function () {
    init_list_table();
    setInterval(function () {
        $("#gameListTable").ajax.reload();
    }, 30000);
});

