<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Formulários e Cálculos</title>
</head>
<body>

<h1>Cálculos Matemáticos e Estatísticos</h1>

<h2>1. Volume da Esfera</h2>
<form method="post">
    Raio: <input type="number" name="raio" required>
    <input type="submit" name="calc_volume" value="Calcular Volume">
</form>
<?php
if (isset($_POST['calc_volume'])) {
    $raio = $_POST['raio'];
    function calcularVolume($r) {
        return (4/3) * pi() * pow($r, 3);
    }
    echo "Volume: " . calcularVolume($raio);
}
?>

<h2>2. Média de Notas</h2>
<form method="post">
    Nota 1: <input type="number" name="nota1" required><br>
    Nota 2: <input type="number" name="nota2" required><br>
    Nota 3: <input type="number" name="nota3" required><br>
    Média: 
    <select name="media">
        <option value="A">Aritmética</option>
        <option value="P">Ponderada</option>
        <option value="H">Harmônica</option>
    </select>
    <input type="submit" name="calc_media" value="Calcular Média">
</form>
<?php
if (isset($_POST['calc_media'])) {
    $n1 = $_POST['nota1'];
    $n2 = $_POST['nota2'];
    $n3 = $_POST['nota3'];
    $tipo_media = $_POST['media'];

    function calcularMedia($n1, $n2, $n3, $tipo) {
        if ($tipo == 'A') {
            return ($n1 + $n2 + $n3) / 3;
        } elseif ($tipo == 'P') {
            return ($n1 * 5 + $n2 * 3 + $n3 * 2) / 10;
        } elseif ($tipo == 'H') {
            return 3 / ((1/$n1) + (1/$n2) + (1/$n3));
        }
    }
    echo "Média: " . calcularMedia($n1, $n2, $n3, $tipo_media);
}
?>

<h2>3. Número Primo</h2>
<form method="post">
    Número: <input type="number" name="numero_primo" required>
    <input type="submit" name="verifica_primo" value="Verificar Primo">
</form>
<?php
if (isset($_POST['verifica_primo'])) {
    $numero = $_POST['numero_primo'];

    function isPrimo($n) {
        if ($n < 2) return false;
        for ($i = 2; $i <= sqrt($n); $i++) {
            if ($n % $i == 0) return false;
        }
        return true;
    }
    echo $numero . " é primo? " . (isPrimo($numero) ? 'Sim' : 'Não');
}
?>

<h2>4. Fórmula de Bhaskara</h2>
<form method="post">
    A: <input type="number" name="a" required><br>
    B: <input type="number" name="b" required><br>
    C: <input type="number" name="c" required><br>
    <input type="submit" name="calc_bhaskara" value="Calcular Raízes">
</form>
<?php
if (isset($_POST['calc_bhaskara'])) {
    $a = $_POST['a'];
    $b = $_POST['b'];
    $c = $_POST['c'];

    function bhaskara($a, $b, $c) {
        $delta = $b * $b - 4 * $a * $c;
        if ($delta < 0) return "Sem raízes reais.";
        $raiz1 = (-$b + sqrt($delta)) / (2 * $a);
        $raiz2 = (-$b - sqrt($delta)) / (2 * $a);
        return "Raízes: $raiz1 e $raiz2";
    }
    echo bhaskara($a, $b, $c);
}
?>

<h2>5. Tempo em Horas, Minutos e Segundos</h2>
<form method="post">
    Tempo (segundos): <input type="number" name="tempo" required>
    <input type="submit" name="calc_tempo" value="Converter">
</form>
<?php
if (isset($_POST['calc_tempo'])) {
    $tempo = $_POST['tempo'];

    function converterTempo($segundos) {
        $horas = floor($segundos / 3600);
        $minutos = floor(($segundos % 3600) / 60);
        $segundos = $segundos % 60;
        return "$horas horas, $minutos minutos e $segundos segundos.";
    }
    echo converterTempo($tempo);
}
?>

<h2>6. Idade em Dias</h2>
<form method="post">
    Anos: <input type="number" name="anos" required><br>
    Meses: <input type="number" name="meses" required><br>
    Dias: <input type="number" name="dias" required><br>
    <input type="submit" name="calc_idade_dias" value="Calcular Dias">
</form>
<?php
if (isset($_POST['calc_idade_dias'])) {
    $anos = $_POST['anos'];
    $meses = $_POST['meses'];
    $dias = $_POST['dias'];

    function idadeEmDias($anos, $meses, $dias) {
        return $anos * 365 + $meses * 30 + $dias; 
    }
    echo "Idade em dias: " . idadeEmDias($anos, $meses, $dias);
}
?>

<h2>7. Número Perfeito</h2>
<form method="post">
    Número: <input type="number" name="numero_perfeito" required>
    <input type="submit" name="verifica_perfeito" value="Verificar Perfeito">
</form>
<?php
if (isset($_POST['verifica_perfeito'])) {
    $numero = $_POST['numero_perfeito'];

    function isPerfeito($n) {
        $soma = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($n % $i == 0) $soma += $i;
        }
        return $soma == $n;
    }
    echo $numero . " é perfeito? " . (isPerfeito($numero) ? 'Sim' : 'Não');
}
?>

<h2>8. Categoria do Nadador</h2>
<form method="post">
    Idade: <input type="number" name="idade_nadador" required>
    <input type="submit" name="calc_categoria" value="Calcular Categoria">
</form>
<?php
if (isset($_POST['calc_categoria'])) {
    $idade = $_POST['idade_nadador'];

    function categoriaNadador($idade) {
        if ($idade >= 5 && $idade <= 7) return "Infantil A";
        elseif ($idade >= 8 && $idade <= 10) return "Infantil B";
        elseif ($idade >= 11 && $idade <= 13) return "Juvenil A";
        elseif ($idade >= 14 && $idade <= 17) return "Juvenil B";
        else return "Adulto";
    }
    echo "Categoria: " . categoriaNadador($idade);
}
?>

<h2>9. Número Positivo ou Negativo</h2>
<form method="post">
    Número: <input type="number" name="numero_pos_neg" required>
    <input type="submit" name="verifica_pos_neg" value="Verificar">
</form>
<?php
if (isset($_POST['verifica_pos_neg'])) {
    $numero = $_POST['numero_pos_neg'];

    function isPositivo($n) {
        return $n >= 0;
    }
    echo $numero . " é positivo? " . (isPositivo($numero) ? 'Sim' : 'Não');
}
?>

<h2>10. Número Par ou Ímpar</h2>
<form method="post">
    Número: <input type="number" name="numero_par_impar" required>
    <input type="submit" name="verifica_par_impar" value="Verificar">
</form>
<?php
if (isset($_POST['verifica_par_impar'])) {
    $numero = $_POST['numero_par_impar'];

    function isPar($n) {
        return $n % 2 == 0;
    }
    echo $numero . " é par? " . (isPar($numero) ? 'Sim' : 'Não');
}
?>

<h2>11. Conceito do Aluno</h2>
<form method="post">
    Média Final: <input type="number" name="media_final" step="0.1" required>
    <input type="submit" name="calc_conceito" value="Calcular Conceito">
</form>
<?php
if (isset($_POST['calc_conceito'])) {
    $media = $_POST['media_final'];

    function conceitoAluno($media) {
        if ($media >= 0 && $media < 5) return 'D';
        elseif ($media >= 5 && $media < 7) return 'C';
        elseif ($media >= 7 && $media < 9) return 'B';
        elseif ($media >= 9 && $media <= 10) return 'A';
        else return 'Nota inválida';
    }
    echo "Conceito: " . conceitoAluno($media);
}
?>

<h2>12. Peso Ideal</h2>
<form method="post">
    Altura (m): <input type="number" step="0.01" name="altura" required><br>
    Sexo: 
    <select name="sexo" required>
        <option value="M">Masculino</option>
        <option value="F">Feminino</option>
    </select>
    <input type="submit" name="calc_peso_ideal" value="Calcular Peso Ideal">
</form>
<?php
if (isset($_POST['calc_peso_ideal'])) {
    $altura = $_POST['altura'];
    $sexo = $_POST['sexo'];

    function pesoIdeal($altura, $sexo) {
        if ($sexo == 'M') {
            return 72.7 * $altura - 58;
        } else {
            return 62.1 * $altura - 44.7;
        }
    }
    echo "Peso Ideal: " . pesoIdeal($altura, $sexo);
}
?>

<h2>13. Ordenar 3 Números</h2>
<form method="post">
    Número 1: <input type="number" name="num1" required><br>
    Número 2: <input type="number" name="num2" required><br>
    Número 3: <input type="number" name="num3" required><br>
    <input type="submit" name="ordena_numeros" value="Ordenar">
</form>
<?php
if (isset($_POST['ordena_numeros'])) {
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $num3 = $_POST['num3'];

    function ordenarNumeros($n1, $n2, $n3) {
        $numeros = [$n1, $n2, $n3];
        sort($numeros);
        return implode(', ', $numeros);
    }
    echo "Números em ordem crescente: " . ordenarNumeros($num1, $num2, $num3);
}
?>

<h2>14. Tipo de Triângulo</h2>
<form method="post">
    Lado X: <input type="number" name="lado_x" required><br>
    Lado Y: <input type="number" name="lado_y" required><br>
    Lado Z: <input type="number" name="lado_z" required><br>
    <input type="submit" name="tipo_triangulo" value="Verificar Triângulo">
</form>
<?php
if (isset($_POST['tipo_triangulo'])) {
    $x = $_POST['lado_x'];
    $y = $_POST['lado_y'];
    $z = $_POST['lado_z'];

    function tipoTriangulo($x, $y, $z) {
        if ($x + $y > $z && $x + $z > $y && $y + $z > $x) {
            if ($x == $y && $y == $z) return "Equilátero";
            elseif ($x == $y || $y == $z || $x == $z) return "Isósceles";
            else return "Escaleno";
        } else {
            return "Não forma um triângulo.";
        }
    }
    echo "Tipo de Triângulo: " . tipoTriangulo($x, $y, $z);
}
?>

</body>
</html>

