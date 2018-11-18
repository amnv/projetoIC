package indexacao;

import java.util.Scanner;

public class Start {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		final String SAIR = "5"; 
		
		String opcao = "";
		do 
		{
			System.out.println("Digite a opção desejada");
			System.out.println("1 - Indexar arquivos");
			System.out.println("2 - Procurar arquivos");
			System.out.println("3 - Salvar ocorrências");
			System.out.println("4 - Salvar ocorrências da lista");
			System.out.println(SAIR + " - Sair");
			opcao = in.nextLine();
			
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
			else if(opcao.equals("3"))
			{
				System.out.println("Digite o termo chave que será pesquisado");
				String docName = in.nextLine();
				try {
					new Save().buildDocument(docName);
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			else if (opcao.equals("4"))
			{
				try {
					new Save().saveFromList();
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			else if (opcao.equals(SAIR)) System.out.println("Saindo!");
			else System.out.println("Digite um valor válido");			
		} while (!opcao.equals(SAIR));
		
		in.close();
	}

}
