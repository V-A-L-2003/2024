<?php
    require "conta.php";
    
$conta = new Conta(1, 'joao', 'CC');
$conta->novaConta();
$conta->dep(200);
$conta->mensal();
$conta->deb(50);
$conta->fechar();


?>