
public class BankAccountTest {
	public static void main(String[] args) {
		BankAccount b = new BankAccount();
		b.getBalance();
		b.deposit(10.00, 29.99);
		b.getBalance();
		b.withdrawal(7.00);
		b.getBalance();
	}
}
