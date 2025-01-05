<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Socorro</title>
</head>
<body>
<?php
#pro serio não passa isso aqui pra mais ninguem é maldade isso não é de deus se eu não estivesse estudando array 
#desde que pisei no campus so não tinha como
$MDistanciaCidades = array(  
    array("Nome", "Pelotas", "Rio Grande", "Guaíba", "São Lourenço", "Poa", "Camaquá"),
    array("Pelotas", '#', "60", "180", "66", "270", "150"),
    array("Rio Grande", "60", '#', "240", "120", "330", "210"),
    array("Guaíba", "180", "240", '#', "40", "150", "150"),
    array("São Lourenço", "66", "120", "40", '#', "186", "60"),
    array("Poa", "270", "330", "150", "186", '#', "270"),
    array("Camaquá", "150", "210", "150", "60", "270", '#')
);
#pq na minha prova ta escrito Samy?
$rota = array(2, 1, 4, 6, 3, 5);

$distanciaTotal = 0;

for ($i = 0; $i < count($rota) - 1; $i++) {
    $cidadeAtual = $rota[$i];
    $proximaCidade = $rota[$i + 1];
    
    $distancia = $MDistanciaCidades[$cidadeAtual][$proximaCidade]; 

    if (is_numeric($distancia)) {
        $distanciaTotal += $distancia;
    } else {
        echo "Distância entre cidade $cidadeAtual e cidade $proximaCidade não definida.<br>";
    }
}
#acredito ter pago meus pecados
echo "A distância total percorrida durante a viagem é: " . $distanciaTotal . " km";
?>  
<h1>
total de 600 pedagios encontrados 
</h1>
<h6>
    na duvida elimina a mais errada prof 🙁
</h6>
<h2>
    sua divida atual é de 3000bi 
    <h1>não fique triste o tigrinho legalizado vai resolver seu problemas vamos apostar</h1>
</h2><form action="" method="post">
    <label for="num1">Número 1:</label>
    <input type="number" name="num1" required min="1" max="60"><br>

    <label for="num2">Número 2:</label>
    <input type="number" name="num2" required min="1" max="60"><br>

    <label for="num3">Número 3:</label>
    <input type="number" name="num3" required min="1" max="60"><br>

    <label for="num4">Número 4:</label>
    <input type="number" name="num4" required min="1" max="60"><br>

    <label for="num5">Número 5:</label>
    <input type="number" name="num5" required min="1" max="60"><br>

    <label for="num6">Número 6:</label>
    <input type="number" name="num6" required min="1" max="60"><br>

    <input type="submit" name="verificar" value="Verificar">
</form>
<h6>
    não escolha a seguite sequencia 10 15 20 25 30 35 assinado bixeiro
</h6>
<?php
if (isset($_POST['verificar'])) {
    $gabarito = [10, 15, 20, 25, 30, 35]; 
    $acertos = 0;

    for ($i = 1; $i <= 6; $i++) {
        $numeroApostado = $_POST['num' . $i];
        if (in_array($numeroApostado, $gabarito)) {
            $acertos++;
        }
    }

  
    echo "Você acertou: $acertos ponto(s).<br>";
    if ($acertos == 6) {
        echo "Você fez uma SENAA (6 acertos)! Parabéns!";
    } elseif ($acertos == 5) {
        echo "Você fez uma QUINA (5 acertos).";
    } elseif ($acertos == 4) {
        echo "Você fez uma QUADRA (4 acertos).";
    } else {
        echo "Infelizmente, você não acertou nenhum número.";
    }
    echo "infelizmente a receita fereal aprendeu qualquer premio que tenha ganhado em razão da sua divida";
}
?>
<h1>Digite uma palavra</h1>
<form action="" method="post">
    <input type="text" name="palavra" required placeholder="Digite uma palavra">
    <input type="submit" value="Enviar">
</form>

<?php
if (isset($_POST['palavra'])) {
    $palavra = $_POST['palavra'];
    $letrasImpares = '';

    for ($i = 0; $i < strlen($palavra); $i++) {
      
        if ($i % 2 != 0) {
            $letrasImpares .= $palavra[$i-1];
        }
    }


    echo "disculpa seu traclado esta ok? aqui chegou " . $letrasImpares;
}
?>
</body>
</html>
