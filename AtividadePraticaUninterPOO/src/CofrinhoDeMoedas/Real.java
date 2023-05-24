package CofrinhoDeMoedas;

public class Real extends Moeda { // classe herdeira ou filha

	public Real(double valor) { // construtor herdado
		super(valor);
	}

	// métodos herdados
	public void info() {
		System.out.println("Real - " + valor);
	}

	public double converter() {
		return valor * 1;
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
