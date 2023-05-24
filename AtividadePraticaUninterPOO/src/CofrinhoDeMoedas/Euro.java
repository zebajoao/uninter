package CofrinhoDeMoedas;

public class Euro extends Moeda { // classe herdeira ou filha

	public Euro(double valor) { // construtor herdado
		super(valor);
	}

	// métodos herdados
	public void info() {
		System.out.println("Euro - " + valor);
	}

	public double converter() {
		return valor * 5.57;
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
