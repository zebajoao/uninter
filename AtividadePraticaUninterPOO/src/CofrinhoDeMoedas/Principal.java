package CofrinhoDeMoedas;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		Cofrinho cofrinho = new Cofrinho(); // instanciando um objeto da classe Cofrinho
		Scanner entradaDeDados = new Scanner(System.in);

		int opcao, tipoMoeda; // variáveis globais
		String valorMoedaEntrada;
		double valorMoeda;

		System.out.println(); // imprimindo um menu inicial
		System.out.println("Menu - Cofrinho");
		System.out.println();
		System.out.println("Selecione uma das opções abaixo:");
		System.out.println("1 - Adicionar moeda;");
		System.out.println("2 - Remover moeda;");
		System.out.println("3 - Listar todas as moedas;");
		System.out.println("4 - Calcular valor total em moedas convertido para Real;");
		System.out.println("0 - Encerrar programa.");
		opcao = entradaDeDados.nextInt();
		System.out.println();

		while (opcao != 0) { // início do processo de verificação da opção escolhida pelo usuário
			switch (opcao) {
			case 1: // primeira opção - adicionar moeda
				while (true) {
					System.out.println("Selecione uma das moedas a seguir:");
					System.out.println("1 - Real;");
					System.out.println("2 - Dólar;");
					System.out.println("3 - Euro;");
					tipoMoeda = entradaDeDados.nextInt();
					System.out.println();
					if (tipoMoeda < 1 || tipoMoeda > 3) { // condição que verifica se a entrada é válida
						System.out.println("Opção inválida!");
						System.out.println();
						continue; // retorna para o início do loop
					} else {
						System.out.println("Digite o valor da moeda:");
						valorMoedaEntrada = entradaDeDados.next(); // recebe tipo de dado string
						System.out.println();
						break;
					}
				}
				valorMoedaEntrada = valorMoedaEntrada.replaceAll(",", "."); // trata as entradas com ","
				valorMoeda = Double.parseDouble(valorMoedaEntrada); // converte o tipo de dado para double
				Moeda novaMoeda;
				if (tipoMoeda == 1) {
					novaMoeda = new Real(valorMoeda); // cria uma instância da classe filha Real
				} else if (tipoMoeda == 2) {
					novaMoeda = new Dolar(valorMoeda); // cria uma instância da classe filha Dolar
				} else {
					novaMoeda = new Euro(valorMoeda); // cria uma instância da classe filha Euro
				}
				cofrinho.adicionar(novaMoeda); // invoca o método "adicionar" da classe Cofrinho
				break;
			case 2: // segunda opção - remover moeda
				while (true) {
					System.out.println("Selecione uma das moedas a seguir:");
					System.out.println("1 - Real;");
					System.out.println("2 - Dólar;");
					System.out.println("3 - Euro;");
					tipoMoeda = entradaDeDados.nextInt();
					System.out.println();
					if (tipoMoeda < 1 || tipoMoeda > 3) {
						System.out.println("Opção inválida!");
						System.out.println();
						continue;
					} else {
						System.out.println("Digite o valor da moeda:");
						valorMoedaEntrada = entradaDeDados.next();
						System.out.println();
						break;
					}
				}
				valorMoedaEntrada = valorMoedaEntrada.replaceAll(",", ".");
				valorMoeda = Double.parseDouble(valorMoedaEntrada);
				Moeda moedaParaRemover;
				if (tipoMoeda == 1) {
					moedaParaRemover = new Real(valorMoeda);
				} else if (tipoMoeda == 2) {
					moedaParaRemover = new Dolar(valorMoeda);
				} else {
					moedaParaRemover = new Euro(valorMoeda);
				}
				cofrinho.remover(moedaParaRemover); // invoca o método "remover" da classe Cofrinho
				break;
			case 3: // terceira opção - listar moedas
				cofrinho.listagemMoedas(); // invoca o método "listagemMoedas" da classe Cofrinho
				break;
			case 4: // quarta opção - calcular total convertido para Real
				cofrinho.totalConvertido(); // invoca o método "totalConvertido" da classe Cofrinho
				break;
			default: // caso o usuário entre com uma opção inválida
				System.out.println("Opção inválida!");
				System.out.println();
			}
			System.out.println();
			System.out.println("Menu - Cofrinho");
			System.out.println();
			System.out.println("Selecione uma das opções abaixo:");
			System.out.println("1 - Adicionar moeda;");
			System.out.println("2 - Remover moeda;");
			System.out.println("3 - Listar todas as moedas;");
			System.out.println("4 - Calcular valor total em moedas convertido para Real;");
			System.out.println("0 - Encerrar programa.");
			opcao = entradaDeDados.nextInt();
			System.out.println();
		}
	}

}
