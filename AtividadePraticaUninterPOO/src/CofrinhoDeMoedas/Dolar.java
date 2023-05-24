package CofrinhoDeMoedas;

public class Dolar extends Moeda { // classe herdeira ou filha

	public Dolar(double valor) { // construtor herdado
		super(valor);
	}

	// métodos herdados
	public void info() {
		System.out.println("Dólar - " + valor);
	}

	public double converter() {
		return valor * 5.38;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		return true;
	}

}
