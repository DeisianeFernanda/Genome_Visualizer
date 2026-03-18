#!/usr/bin/env python3
"""
Visualizador de Genomas - Ferramenta de linha de comando
Uso: visualizador [opções]
"""

import os
import sys
import subprocess
import argparse

def main():
    # Argumentos de linha de comando (igual ferramentas reais!)
    parser = argparse.ArgumentParser(
        description="🧬 Visualizador de Genomas - Dashboard interativo para DNA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  visualizador                    # Abre o dashboard
  visualizador --port 8502        # Abre em porta específica
  visualizador --help              # Mostra esta ajuda
  visualizador --version           # Mostra versão
        """
    )
    
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=8501,
        help="Porta para executar o servidor (default: 8501)"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="store_true",
        help="Mostra versão do programa"
    )
    
    args = parser.parse_args()
    
    if args.version:
        print("Visualizador de Genomas v1.0.0")
        print("Desenvolvido com Streamlit e Biopython")
        sys.exit(0)
    
    # Caminho absoluto para o app
    app_path = os.path.expanduser("~/visualizador_de_genomas/app.py")
    
    # Verifica se o arquivo existe
    if not os.path.exists(app_path):
        print(f"❌ Erro: Arquivo não encontrado em {app_path}")
        print("Verifique o caminho ou crie um link simbólico:")
        print("  ln -s /seu/caminho/real/app.py ~/visualizador_de_genomas/app.py")
        sys.exit(1)
    
    # Executa o streamlit
    print(f"🧬 Iniciando Visualizador na porta {args.port}...")
    cmd = ["streamlit", "run", app_path, "--server.port", str(args.port)]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 Visualizador encerrado.")
        sys.exit(0)

if __name__ == "__main__":
    main()