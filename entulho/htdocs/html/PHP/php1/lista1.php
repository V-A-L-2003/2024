<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resolução Preguiçosa</title>
</head>
<body>
    <h1>Resolução Preguiçosa</h1>
    <form method="POST">
        <!-- Questão 1 -->
        <label>Número (Positivo, Negativo ou Zero):</label>
        <input type="number" name="num1"><br>

        <!-- Questão 2 -->
        <label>Número para Tabuada:</label>
        <input type="number" name="numTabuada"><br>

        <!-- Questão 3 -->
        <label>Número para Fatorial:</label>
        <input type="number" name="numFatorial"><br>

        <!-- Questão 4 -->
        <label>Escolha uma Operação:</label>
        <select name="operacao">
            <option value="soma">Soma</option>
            <option value="subtracao">Subtração</option>
            <option value="multiplicacao">Multiplicação</option>
            <option value="divisao">Divisão</option>
        </select><br>
        <label>Número 1:</label>
        <input type="number" name="numA">
        <label>Número 2:</label>
        <input type="number" name="numB"><br>

        <!-- Questão 5 -->
        <label>Número para verificar Par ou Ímpar:</label>
        <input type="number" name="numParImpar"><br>

        <!-- Questão 6 -->
        <label>Valor A:</label>
        <input type="number" name="valorA">
        <label>Valor B:</label>
        <input type="number" name="valorB"><br>

        <!-- Questão 7 -->
        <label>Valor A:</label>
        <input type="number" name="maiorMenorA">
        <label>Valor B:</label>
        <input type="number" name="maiorMenorB"><br>

        <!-- Questão 8 -->
        <label>Nota 1:</label>
        <input type="number" name="nota1">
        <label>Nota 2:</label>
        <input type="number" name="nota2">
        <label>Nota 3:</label>
        <input type="number" name="nota3"><br>

        <!-- Questão 9 -->
        <label>Seu Nome:</label>
        <input type="text" name="nome">
        <label>Sua Idade:</label>
        <input type="number" name="idade"><br>

        <!-- Questão 10 -->
        <label>Número do Mês:</label>
        <input type="number" name="numMes"><br>

        <button type="submit" name="submit">Enviar</button>
    </form>

    <?php
    if (isset($_POST['submit'])) {
        // Questão 1
        $num1 = $_POST['num1'];
        if ($num1 > 0) {
            echo "<p>Valor Positivo</p>";
        } elseif ($num1 < 0) {
            echo "<p>Valor Negativo</p>";
        } else {
            echo "<p>Igual a Zero</p>";
        }

        // Questão 2
        $numTabuada = $_POST['numTabuada'];
        echo "<p>Tabuada do $numTabuada:</p>";
        for ($i = 0; $i <= 10; $i++) {
            echo "<p>$numTabuada x $i = " . ($numTabuada * $i) . "</p>";
        }

        // Questão 3
        $numFatorial = $_POST['numFatorial'];
        $fatorial = 1;
        for ($i = $numFatorial; $i >= 1; $i--) {
            $fatorial *= $i;
        }
        echo "<p>Fatorial de $numFatorial = $fatorial</p>";

        // Questão 4
        $numA = $_POST['numA'];
        $numB = $_POST['numB'];
        $operacao = $_POST['operacao'];
        switch ($operacao) {
            case 'soma':
                echo "<p>Resultado: " . ($numA + $numB) . "</p>";
                break;
            case 'subtracao':
                echo "<p>Resultado: " . ($numA - $numB) . "</p>";
                break;
            case 'multiplicacao':
                echo "<p>Resultado: " . ($numA * $numB) . "</p>";
                break;
            case 'divisao':
                if ($numB != 0) {
                    echo "<p>Resultado: " . ($numA / $numB) . "</p>";
                } else {
                    echo "<p>Não pode dividir por zero!</p>";
                }
                break;
        }

        // Questão 5
        $numParImpar = $_POST['numParImpar'];
        if ($numParImpar % 2 == 0) {
            echo "<p>$numParImpar é Par</p>";
        } else {
            echo "<p>$numParImpar é Ímpar</p>";
        }

        // Questão 6
        $valorA = $_POST['valorA'];
        $valorB = $_POST['valorB'];
        if ($valorA < $valorB) {
            echo "<p>Ordem crescente: $valorA, $valorB</p>";
        } else {
            echo "<p>Ordem crescente: $valorB, $valorA</p>";
        }

        // Questão 7
        $maiorMenorA = $_POST['maiorMenorA'];
        $maiorMenorB = $_POST['maiorMenorB'];
        if ($maiorMenorA > $maiorMenorB) {
            echo "<p>A maior que B</p>";
        } else {
            echo "<p>A menor que B</p>";
        }

        // Questão 8
        $nota1 = $_POST['nota1'];
        $nota2 = $_POST['nota2'];
        $nota3 = $_POST['nota3'];
        $media = ($nota1 + $nota2 + $nota3) / 3;
        if ($media >= 6) {
            echo "<p>Média = $media [Aprovado]</p>";
        } else {
            echo "<p>Média = $media [Reprovado]</p>";
        }

        // Questão 9
        $nome = $_POST['nome'];
        $idade = $_POST['idade'];
        if ($idade >= 18) {
            echo "<p>$nome é maior de 18 e tem $idade anos.</p>";
        } else {
            echo "<p>$nome não é maior de 18 e tem $idade anos.</p>";
        }

        // Questão 10
        $numMes = $_POST['numMes'];
        $meses = [
            1 => "Janeiro", 2 => "Fevereiro", 3 => "Março", 4 => "Abril",
            5 => "Maio", 6 => "Junho", 7 => "Julho", 8 => "Agosto",
            9 => "Setembro", 10 => "Outubro", 11 => "Novembro", 12 => "Dezembro"
        ];
        if (isset($meses[$numMes])) {
            echo "<p>Mês correspondente: " . $meses[$numMes] . "</p>";
        } else {
            echo "<p>Não existe mês com esse número</p>";
        }
    }
    ?>
</body>
</html>
