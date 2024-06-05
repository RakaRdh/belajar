// alert(
//     "Jenis-jenis Wibu di 2SE1 : \n"+
//     "1. Wibu Baby Blues \n"+
//     "2. Wibu Pemakan Ternak Warga \n"+
//     "3. Wibu Denial \n"+
//     "4. Wibu Tak Tertolong \n"
// );

var nama = prompt("Masukkan nama Anda");
var usia = prompt("Masukkan usia Anda");
cekidot();

function cekidot(){
    if(nama == ""){
        alert("kosong bre nama lu");
    }else if(usia == ""){
        alert("mana usia lu bre");
    }else if (usia > 18){
        alert("Nama anda " +nama+ ", Usia Anda " + usia + ", Anda Major");
    }else{
        alert("Nama anda " +nama+ ", Usia Anda " + usia + ", Anda Minor");
    }
}