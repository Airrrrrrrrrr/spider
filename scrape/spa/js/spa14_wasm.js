 function encrypt(a,b){
	 return Math.floor(b/3 + a + 16358)
 }
 function getSign(num){
var n = (num - 1) * 10
 , e = encrypt(n, parseInt(Math.round((new Date).getTime() / 1e3).toString()));
 console.log(e)
 }
 getSign(1)
