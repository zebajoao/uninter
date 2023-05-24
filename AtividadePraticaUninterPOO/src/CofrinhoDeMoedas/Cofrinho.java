package CofrinhoDeMoedas;

import java.util.ArrayList;

public class Cofrinho {
	// lista que armazenará objetos de diferentes "tipos"
	private ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();

	public void adicionar(Moeda x) { // método que adiciona uma moeda no ArrayList
		listaMoedas.add(x);
	}

	public void remover(Moeda x) { // método que remove uma moeda do ArrayList
		listaMoedas.remove(x);
	}

	public void listagemMoedas() { // método que lista as moedas presentes na lista
		for (Moeda x : listaMoedas) {
			x.info();
		}
	}

	public void totalConvertido() { // método que calcula o valor total das moedas convertido para Real
		double soma = 0;
		for (Moeda x : listaMoedas) {
			soma += x.converter();
		}
		System.out.printf("O total convertido para Real é R$%.2f", soma);
		System.out.println();
	}

}
