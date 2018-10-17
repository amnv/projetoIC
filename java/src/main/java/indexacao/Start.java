package indexacao;

import java.util.Scanner;

public class Start {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		System.out.println("Digite a opção desejada");
		System.out.println("1 - Indexar arquivos");
		System.out.println("2 - Procurar arquivos");
		String opcao = in.nextLine();
		
		if (opcao.equals("1"))
		{
			Indexacao indexacao = new Indexacao();
			indexacao.indexar();
			
		}
		else if (opcao.equals("2"))
		{
			Search search = new Search();
			try {
				search.searching();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else System.out.println("Digite um valor válido");
		
		in.close();
	}

}
