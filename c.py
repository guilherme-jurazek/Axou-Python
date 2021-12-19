# include<conio.h>
# include<stdlib.h>
# include<stdio.h>
# include<windows.h>
# include<ctype.h>
# include<string.h>


int
main()
{

float conta, resp;
char op;
op = 'S';
do
{

        system("cls");
    printf("Estacao do ano em que a analise foi feita:\n");
    printf("1- Inverno.\n");
    printf("2- Primavera.\n");
    printf("3- Verao.\n");
    printf("4- Outono.\n");
    do
    {
        printf("\nResposta: ");
    scanf("%f", & resp);
    }
        while (resp < 1 | | resp > 4);
        if (resp <= 2){
            system("cls");

            printf("Numeros de horas gastas ocioso:\n");
            printf("\nResposta: ");
            scanf("%f", & resp);
            conta = resp / 24;
            resp = conta;

            if (resp <= 0.47)
                printf("\n\nDiagnostico normal: 100%% de ser fertil.");
            else {
                system("cls");
                printf("Idade na epoca da analise:  ");
                printf("\nResposta: ");
                scanf("%f", & resp);
                conta = resp / 36;
                resp = conta;

                if (resp > 0.67)
                    printf("\n\nDiagnostico normal: 100%% de ser fertil.");
                else if (resp <= 0.67 & & resp > 0.61)
                    printf("\n\nDiagnostico: 50%% de ser fertil.");
                else {
                    system("cls");
                    printf("Numeros de horas gastas ocioso:\n");
                    printf("\nResposta: ");
                    scanf("%f", & resp);
                    conta = resp / 24;
                    resp = conta;

                    if (resp > 0.75)
                        printf("\n\nDiagnostico: 50%% de ser fertil.");
                    else
                        printf("\n\nDiagnostico normal: 100%% de ser fertil.");
                    }
                }

            }
        else {
            system("cls");
            printf("Idade na epoca da analise:  ");
            printf("\nResposta: ");
            scanf("%f", & resp);
            conta = resp / 36;
            resp = conta;

            if (resp > 0.67){
                system("cls");
                printf("Com qual frequencia voce costuma fumar?:\n");
                printf("1- Nunca.\n");
                printf("2- Ocasionalmente.\n");
                printf("3- Diariamente.\n");
                printf("Resposta:");
                scanf("%f", & resp);

                if (resp == 1)
                    printf("\n\nDiagnostico alterado: 25%% de ser fertil.");
                else
                    printf("\n\nDiagnostico normal: 100% de ser fertil.");
                }
        else {
            system("cls");
            printf("Numeros de horas gastas ocioso:\n");
            printf("\nResposta: ");
            scanf("%f", & resp);
            conta = resp / 24;
            resp = conta;

            if (resp <= 0.31)
                printf("\n\nDiagnostico normal: 100%% de ser fertil.");
            else {
                system("cls");
                printf("Idade na epoca da analise:  ");
                printf("\nResposta: ");
                scanf("%f", & resp);
                conta = resp / 36;
                resp = conta;

                if (resp > 0.64)
                    printf("\n\nDiagnostico alterado: 0%% de ser fertil.");
                else
                    printf("\n\nDiagnostico normal: 100%% de ser fertil.");
                }

            }

        }

        printf("\n\nDeseja fazer novamente?(S/N)\n");
        printf("Resposta:");
        fflush(stdin);
        scanf("%c", & op);
        }while (toupper(op) == 'S');
        }