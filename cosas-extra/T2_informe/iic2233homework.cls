% \NeedsTeXFormat{LaTeX2e}
\ProvidesClass{iic2233homework}[2018/08/05 IIC2233 homework class]
\LoadClass[11pt]{extarticle}

\RequirePackage{fullpage}
\RequirePackage[letterpaper, margin=2cm]{geometry}
\RequirePackage[T1]{fontenc}
\RequirePackage[spanish]{babel}
%----------------------------- TEXTO ---------------------------
\RequirePackage{parskip}                    % Permite separar los párrafos
\RequirePackage{xspace}                     % Agregar espacios automáticamente después de las palabras comandos
\RequirePackage{dirtytalk}                  % Poner cosas entre comillas fácilmente: \say{algo que va entre comillas}
\RequirePackage{ulem}                       % Tachar texto
\RequirePackage{bold-extra}                 % Monoespaciado con negrilla
\RequirePackage{textcomp}                   % Símbolos: $, copyright, ...
%-------------------------- ECUACIONES --------------------------
\RequirePackage{amsmath}                    % Ambientes para ecuaciones
\RequirePackage{amssymb}                    % Símbolos matemáticos
\RequirePackage{mathtools}                  % Símbolos matemáticos amsmath
%--------------------------- IMÁGENES ---------------------------
\RequirePackage{float}                      % Posicionar figuras: H, h!, b...
\RequirePackage{graphicx}                   % Agregar características a las imágenes 
\RequirePackage{epsfig}                     % Paquete relacionado con graphicx (es una especie de envoltorio)
\RequirePackage{caption}                    % Agregar caption a las figuras
\RequirePackage{subcaption}                 % Agregar caption a las subfiguras
\RequirePackage{epstopdf}                   % Permite agregar .eps al enunciado
%---------------------------- TABLAS ----------------------------
\RequirePackage{tabularx}                   % Permite juntar celdas en las tablas
\RequirePackage{booktabs}                   % Tablas bonitas: toprule, midrule, bottomrule
%---------------------------- CÓDIGO ----------------------------
\RequirePackage{minted}                     % Código monoespaciado de color
%----------------------------- COLOR ----------------------------
\RequirePackage{color}                      % Crear y agregar colores
%----------------------------- OTROS ----------------------------
\RequirePackage{ifthen}                     % Hacer if dentro de latex
\RequirePackage{enumitem}                   % Permite personalizar enumerate, itemize y description
\RequirePackage{dirtree}                    % Generar el árbol de directorios
\RequirePackage[hidelinks]{hyperref}        % Permite remover el color y borde de los links
\RequirePackage{fontspec}                   % Agregar fuentes
% \RequirePackage{scrextend}                % Para hacer hacer referencia a un footnote en varias partes del texto. 
                                            % IMPORTAR SOLO SI ES NECESARIO

\newfontfamily{\NotoEmoji}{NotoColorEmoji.ttf}[Renderer=Harfbuzz, Path = resources/]
\newcommand{\const}[1]{\textcolor{blue(munsell)}{\MakeUppercase{\texttt{#1}}}}% Fuente para emojis

%----------------------------------------------------------------------

% Parameters
\def\homeworknumber#1{\def\@homeworknumber{#1}}
\def\semester#1{\def\@semester{#1}}
\def\year#1{\def\@year{#1}}
\def\folder{Tareas/T\@homeworknumber/}
\def\homeworkname{T\@homeworknumber/}

%----------------------------------------------------------------------

% Default values
\parindent 0pt                              % No indentation paragraphs

%----------------------------------------------------------------------

% Minted
\newminted[python]{python}{linenos,frame=single}            % Use \begin{python}code\end{python}
\newminted[pythonplain]{python}{frame=none}                 % Use \begin{python}code\end{python}
\newmintedfile[pythoninput]{python}{linenos,frame=single}   % Use \pythoninput{file.py}
\newcommand{\mil}[1]{\mintinline{python}{#1}}

%----------------------------------------------------------------------

% Shortcuts
\newcommand{\link}[2]{{\color{blue}{\href{#1}{\textbf{\underline{#2}}}}}}
\newcommand{\fullref}[1]{\hyperref[{#1}]{\autoref*{#1}: \nameref*{#1}}}
%\newcommand{\const}[1]{\textcolor{blue(munsell)}{\MakeUppercase{\texttt{#1}}}}
\newcommand{\emoji}[1]{{\NotoEmoji \symbol{"#1}}}           % Emoji command

%----------------------------------------------------------------------

% Config to put titles and "entrega" sections automatically
\newcommand{\makepucheader}{
    \noindent\begin{tabular}{ll}
    \includegraphics[height=2.5cm]{resources/puclogo.eps}
    &
    \begin{minipage}[b]{\textwidth}
    \noindent\textsc{Pontificia Universidad Católica de Chile\\
    Escuela de Ingeniería\\
    Departamento de Ciencia de la Computación\\    
    }
    \end{minipage}
    \end{tabular}
}
\newcommand{\makehomeworktitle}{
    \begin{center}
    {\small\bf IIC2233 Programación Avanzada (\@year-\@semester)} \\
    \vspace{3ex}
    \textbf{\Huge Tarea~\@homeworknumber}
    \end{center}
    \input{preamble.tex}
}

\AtBeginDocument{
    \makepucheader
    \makehomeworktitle
}
\AtEndDocument{
     \input{postamble.tex}
}

%----------------------------------------------------------------------

% COLORES
\definecolor{black}{rgb}{0.0, 0.0, 0.0}
\definecolor{copper}{rgb}{0.72, 0.45, 0.2}
\definecolor{darkgreen}{rgb}{0.05, 0.6, 0.05}
\definecolor{purple}{rgb}{0.4,0.3,0.8}
\definecolor{darkorange}{rgb}{1.0, 0.35, 0.0}
\definecolor{wine}{rgb}{0.8, 0.4, 0.4}
\definecolor{piscola}{rgb}{0.75, 0.30, 0.12}
\definecolor{negroni}{rgb}{0.85, 0.10, 0.01}
\definecolor{amber-ale}{rgb}{0.90, 0.45, 0.05}
\definecolor{indianyellow}{rgb}{0.89, 0.66, 0.34}
\definecolor{codegray}{rgb}{0.9,0.9,0.9}
\definecolor{tequila}{rgb}{0.7412,0.4235,0.3529}
\definecolor{azulpatrio}{rgb}{0, 0.21, 0.68}
\definecolor{verdebienchillon}{rgb}{0.55, 0.74, 0.01}
\definecolor{blue(munsell)}{rgb}{0.0, 0.5, 0.69}
\definecolor{blue(ncs)}{rgb}{0.0, 0.53, 0.74}
\definecolor{azul-benja}{rgb}{0, 0, 1}
\definecolor{greenradar}{rgb}{0.57, 0.76, 0.49}
\definecolor{mauvetaupe}{rgb}{0.57, 0.37, 0.43}
\definecolor{teal}{rgb}{0.25, 0.875, 0.8125}
\definecolor{gray}{rgb}{0.65, 0.65, 0.65}
\definecolor{mediumorchid}{rgb}{0.73, 0.33, 0.83}
\definecolor{turquesita}{rgb}{0.19, 0.84, 0.78}
\definecolor{blue(ncs)}{rgb}{0.0, 0.53, 0.74}
\definecolor{teal}{rgb}{0.25, 0.875, 0.8125}
\definecolor{azul-cris}{rgb}{0.2,0.42,0.76}
\definecolor{watermelon}{rgb}{0.93, 0.16, 0.33}
\definecolor{cobalto}{rgb}{0.52, 0.65, 0.96}
\definecolor{emerald}{rgb}{0.44,0.84,0.62}
\definecolor{primaryColor}{rgb}{0.937, 0.424, 0}

\newcommand{\com}[3]{{\colorbox{#2}{\bfseries\sffamily\scriptsize\textcolor{white}{#1}}}
{\textcolor{#2}{\sf\small\textit{#3}}}}

% COMENTARISTAS
%\newcommand{\dante}[1]{\com{Dante}{blue(ncs)}{#1}}
%\newcommand{\hernan}[1]{\com{Hernan}{darkorange}{#1}}
%\newcommand{\dan}[1]{\com{Dani}{verdebienchillon}{#1}}
%\newcommand{\cris}[1]{\com{Cris}{azul-cris}{#1}}
%\newcommand{\pia}[1]{\com{Pia}{watermelon}{#1}}
%\newcommand{\gery}[1]{\com{Gery}{magenta}{#1}}
%\newcommand{\benjeh}[1]{\com{Benjeh}{blue}{#1}}
%\newcommand{\diego}[1]{\com{Diego}{blue}{#1}}
%\newcommand{\esteban}[1]{\com{Esteban}{blue}{#1}}
%\newcommand{\nati}[1]{\com{Nati}{cobalto}{#1}}
%\newcommand{\cata}[1]{\com{Cata}{emerald}{#1}}

\newcommand{\enfasis}[1]{\textcolor{primaryColor}{\textbf{#1}}}
\newcommand{\noModificar}{{\colorbox{gray}{ {\parbox{4.3em}{\centering\bfseries\sffamily\scriptsize\textcolor{white}{No modificar}}} } }}
\newcommand{\modificar}{{\colorbox{darkgreen}{ {\parbox{4.3em}{\centering\bfseries\sffamily\scriptsize\textcolor{white}{Modificar}}} } }}



% tarea 2 2025-1
    \newcommand{\paca}[1]{\com{paca}{greenradar}{#1}} %encargada
    \newcommand{\fran}[1]{\com{Fran}{mediumorchid}{#1}} %revision
    \newcommand{\claudio}[1]{\com{Claudio}{turquesita}{#1}} %coord
    %redactores
    \newcommand{\Luc}[1]{\com{Luc}{copper}{#1}}
    \newcommand{\Victor}[1]{\com{Victor}{mediumorchid}{#1}}
    \newcommand{\Maira}[1]{\com{Maira}{tequila}{#1}}
    \newcommand{\Enzo}[1]{\com{Enzo}{wine}{#1}}