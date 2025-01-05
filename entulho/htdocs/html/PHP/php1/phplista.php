<form name="form_contato" method="post" action="">
    <div>
        <label>Numero A:  
            <input type="text" name="sinal" id="id_A" placeholder="Insira seu numero" size="30" maxlength="50" required>
        </label>
        <br>
        <label>Numero B:
            <input type="text" name="numB" placeholder="Insira outro numero">
        </label>
        <br>
        <label>Escolha a operação:
            <select name="operation">
                <option value="soma">Soma</option>
                <option value="subtração">Subtração</option>
                <option value="multiplicação">Multiplicação</option>
                <option value="divisão">Divisão</option>
            </select>
        </label>
        <br>
        <label>Nota 1:
            <input type="text" name="nota1" placeholder="Insira Nota 1">
        </label>
        <br>
        <label>Nota 2:
            <input type="text" name="nota2" placeholder="Insira Nota 2">
        </label>
        <br>
        <label>Nota 3:
            <input type="text" name="nota3" placeholder="Insira Nota 3">
        </label>
        <br>
        <label>Nome:
            <input type="text" name="nome" placeholder="Insira seu nome">
        </label>
        <br>
        <label>Idade:
            <input type="text" name="idade" placeholder="Insira sua idade">
        </label>
        <br>
        <input type="submit" name="botaoSubmit" value="Enviar Mensagem">
        <input type="reset" name="botaoReset" value="Limpar Campos">
    </div>
</form>

<?php
if (isset($_POST['botaoSubmit'])) {
    $num = $_POST['sinal'];

    // Task 1: Check if number is positive, negative, or zero
    if ($num > 0) {
        echo "Num $num é positivo<br>";
    } elseif ($num < 0) {
        echo "Num $num é negativo<br>";    
    } else {
        echo "Número é igual a zero<br>";
    }

    // Task 2: Multiplication table of the number
    echo "<h3>Tabuada de $num:</h3>";
    for ($i = 0; $i <= 10; $i++) {
        echo "$num x $i = " . ($num * $i) . "<br>";
    }

    // Task 3: Factorial calculation
    $factorial = 1;
    for ($i = 1; $i <= $num; $i++) {
        $factorial *= $i;
    }
    echo "Fatorial de $num é: $factorial<br>";

    // Task 4: Simple calculator (soma, subtração, multiplicação, divisão)
    if (isset($_POST['numB']) && isset($_POST['operation'])) {
        $num2 = $_POST['numB'];
        $operation = $_POST['operation'];
        switch ($operation) {
            case 'soma':
                echo "Resultado: " . ($num + $num2) . "<br>";
                break;
            case 'subtração':
                echo "Resultado: " . ($num - $num2) . "<br>";
                break;
            case 'multiplicação':
                echo "Resultado: " . ($num * $num2) . "<br>";
                break; 
            case 'divisão':
                if ($num2 == 0) {
                    echo 'Não existe número dividido por zero<br>';
                } elseif ($num == 0) {
                    echo 'O número não pode ser dividido por zero<br>';
                } else {
                    echo "Resultado: " . ($num / $num2) . "<br>";
                }
                break;
        }
    }

    // Task 5: Check if the number is even or odd
    if ($num % 2 == 0) {
        echo "$num é par<br>";
    } else {
        echo "$num é ímpar<br>";
    }

    // Task 6: Order two numbers
    if (isset($_POST['sinal']) && isset($_POST['numB'])) {
        $numA = $num;
        $numB = $_POST['numB'];
        if ($numA > $numB) {
            echo "$numB $numA<br>";
        } else {
            echo "$numA $numB<br>";
        }
    }

    // Task 7: Compare two numbers
    if (isset($_POST['sinal']) && isset($_POST['numB'])) {
        $A = $num;
        $B = $_POST['numB'];
        if ($A > $B) {
            echo "A é maior que B<br>";
        } else {
            echo "A é menor que B<br>";
        }
    }

    // Task 8: Calculate average
    if (isset($_POST['nota1']) && isset($_POST['nota2']) && isset($_POST['nota3'])) {
        $notas = [$_POST['nota1'], $_POST['nota2'], $_POST['nota3']];
        $media = array_sum($notas) / count($notas);
        echo "Média final: $media - " . ($media >= 6 ? "Aprovado" : "Reprovado") . "<br>";
    }

    // Task 9: Name and age check
    if (isset($_POST['nome']) && isset($_POST['idade'])) {
        $nome = $_POST['nome'];
        $idade = $_POST['idade'];
        echo "$nome " . ($idade >= 18 ? "é maior de 18" : "não é maior de 18") . " e tem $idade Anos<br>";
    }

    // Task 10: Month from number
    if ($num >= 1 && $num <= 12) {
        $months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
        echo "Mês correspondente: " . $months[$num - 1] . "<br>";
    } else {
        echo "Não existe mês com esse número.<br>";
    }
}
?>
