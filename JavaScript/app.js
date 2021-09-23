var mysql = require("mysql");
var connection = mysql.createConnection({
host: "XXXXXX",
user: "root",
password: "********",
port: 3306,
database : "xrhTest",
charset : "utf8"
});
connection.connect();
var sql = "select * from tb_stu1;";
connection.query(sql,function(err,result){
    // if (err) throw err;
    console.log(result);
});
connection.end();