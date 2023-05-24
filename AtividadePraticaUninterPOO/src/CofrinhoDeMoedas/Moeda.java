package CofrinhoDeMoedas;

public abstract class Moeda { // classe mãe abstrata
	double valor; // atributo da classe

	public Moeda(double valor) { // construtor
		super();
		this.valor = valor;
	}

	abstract public void info(); // método que imprimirá informações da moeda

	abstract public double converter(); // método que converterá o valor da moeda para Real

	@Override
	public boolean equals(Object obj) { // método que permite realizar comparações entre objetos
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Moeda other = (Moeda) obj;
		if (Double.doubleToLongBits(valor) != Double.doubleToLongBits(other.valor))
			return false;
		return true;
	}

}
