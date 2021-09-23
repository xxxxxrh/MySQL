var mysql = require("mysql");
var connection = mysql.createConnection({
host: "47.114.110.135",
user: "root",
password: "Xrh981025",
port: 3306,
database : "xrhTest",
charset : "utf8"
});
connection.connect();
var sql = "select * from tb_stu1;";
connection.query(sql,function(err,result){
    if (err) throw err;
    console.log(result);
});
connection.end();