<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<p>irei calcular pra vc não ter que passar trabalho</p>
<h1>CAlCULADORA</h1>

<form name="form_contato" method="post"
 action="">

<div>
    <label>Numero A:  
        <input type="text" name="A" id="id_A" placeholder="Insira seu numero" size="30" maxlength="50" required>
   </label>
        <br>
    <label>Numero B:  
        <input type="text" name="B" id="id_B" placeholder="Insira seu numero" size="30" maxlength="50" required>
   </label>
   <input type="submit" name="botaoSubmit" value="Enviar Mensagem" onclick="alert('Mensagem enviada com sucesso!');">
    <input type="reset" name="botaoReset" value="Limpar Campos">
</div>
<h2>Resultado</h2>
<?php
if (isset($_POST['botaoSubmit'])){
$A = $_POST['A'];
$B = $_POST['B'];
$C = $A + $B;
if ($A = 0) {
echo 'aceitamos zero aqui amigo';
}
elseif ($B == 0) {
echo 'aceitamos zero aqui amigo';
}
else {
echo $C;
}
}
?>
</body>
</html>