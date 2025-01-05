<?php
class Conta {
    private $id;
    private $user;
    private $saldo;
    private $score;
    private $tipo;
    private $ativa;

    function __construct($id, $user, $tipo, $saldo = 0, $score = 0, $ativa = true) {
        $this->id = $id;
        $this->user = $user;
        $this->tipo = $tipo;
        $this->saldo = $saldo;
        $this->score = $score;
        $this->ativa = $ativa;

        if ($this->tipo == 'CC' && $this->saldo < 50) {
            $this->saldo = 50;
        } elseif ($this->tipo == 'CP' && $this->saldo < 100) {
            $this->saldo = 100;
        }
    }

    public function novaConta() {
        if ($this->tipo == 'CC' && $this->saldo < 50) {
            $this->saldo = 50;
        } elseif ($this->tipo == 'CP' && $this->saldo < 100) {
            $this->saldo = 100;
        }
        echo "Conta {$this->tipo} de {$this->user} criada com saldo: R$ {$this->saldo}.<br>";
    }

    public function fechar() {
        if ($this->saldo == 0) {
            $this->ativa = false;
            echo "Conta de {$this->user} fechada.<br>";
        } else {
            echo "Não é possível fechar a conta. Saldo não é zero.<br>";
        }
    }

    public function dep($valor) {
        if ($this->ativa) {
            $this->saldo += $valor;
            echo "Depósito de R$ {$valor}. Saldo: R$ {$this->saldo}.<br>";
        } else {
            echo "Conta inativa. Depósito não realizado.<br>";
        }
    }

    public function deb($valor) {
        if ($this->ativa) {
            if ($this->saldo >= $valor) {
                $this->saldo -= $valor;
                echo "Débito de R$ {$valor}. Saldo: R$ {$this->saldo}.<br>";
            } else {
                echo "Saldo insuficiente.<br>";
            }
        } else {
            echo "Conta inativa. Débito não realizado.<br>";
        }
    }

    public function mensal() {
        if ($this->ativa) {
            $mensalidade = ($this->tipo == 'CC') ? 10 : 12;
            if ($this->saldo >= $mensalidade) {
                $this->saldo -= $mensalidade;
                echo "Mensalidade de R$ {$mensalidade} paga. Saldo: R$ {$this->saldo}.<br>";
            } else {
                echo "Saldo insuficiente para mensalidade.<br>";
            }
        } else {
            echo "Conta inativa. Mensalidade não paga.<br>";
        }
    }

    public function getId() {
        return $this->id;
    }

    public function setId($id) {
        $this->id = $id;
    }

    public function getUser() {
        return $this->user;
    }

    public function setUser($user) {
        $this->user = $user;
    }

    public function getSaldo() {
        return $this->saldo;
    }

    public function setSaldo($saldo) {
        $this->saldo = $saldo;
    }

    public function getScore() {
        return $this->score;
    }

    public function setScore($score) {
        $this->score = $score;
    }

    public function getTipo() {
        return $this->tipo;
    }

    public function setTipo($tipo) {
        $this->tipo = $tipo;
    }

    public function getAtiva() {
        return $this->ativa;
    }

    public function setAtiva($ativa) {
        $this->ativa = $ativa;
    }
}

