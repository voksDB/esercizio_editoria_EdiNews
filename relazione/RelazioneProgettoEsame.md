---
title: Relazione del progetto d'esame "EdiNews"
author: Damon Bianchi 943675
date: 2025-07-04
institute: Università degli Studi di Milano
course: Editoria Digitale
tags:
  - python
  - yaml
  - markdown
  - hugo
  - news
version: 0.1
kind: Document
bibliography: bibliografia.bib
csl: IEEE.csl
---

![](img/minerva.png)

# EdiNews

Raccolta di _sintesi_ e _analisi_ sui principali temi di attualità 

## Introduzione

il progetto ha l'obbiettivo di creare un contenuto editoriale accessibile a giornalisti e operatori dell'informazione che riassuma il risultato dei più recenti studi su un determinato argomento. 

il progetto utilizza il framework _Hugo_ per raccogliere e diffondere tramite un sito web statico il contenuto prodotto. 

Il processo ha previsto l'acquisizione e strutturazione di contenuti in _markdown_, e la pubblicazione automatizzata tramite script python su: [EdiNews](https://voksdb.github.io/esercizio_editoria_EdiNews/posts/clima_salute_mentale/), dove ogni articolo è disponibile per il download in formato pdf e .md, oltre che alla lettura online. 

## Ideazione 

### Tema

i temi affrontati negli articoli pubblicati riguarderanno temi come  salute globale, intelligenza artificiale, crisi climatica, agricoltura sostenibile.  

per questi temi è fondamentale l'accesso alla letteratura scientifica e il confronto tra fonti differenti, ma non sempre negli articoli giornalistici pubblicati  è chiaro quali studi siano stati presi come riferimento, creando il rischio di generare disinformazione. 

il progetto ha l'obbiettivo di rendere chiara, rapida e accessibile l'informazione su questi temi, sintetizzando e confrontando alcuni recenti articoli sull'argomento. 

![](img/edinews.png)

### Destinatari

- **Anna**, 29 anni, scrittrice freelance per una testata online. Scrive pezzi divulgativi su salute e scienza, cerca fonti verificabili, attraverso il materiale pubblicato potrà facilmente analizzare gli articoli scientifici sull'argomento 

- **Alessandro**, 45 anni, caporedattore di una rivista scientifica mensile. Vuole inserire rapidi aggiornamenti nel prossimo numero.

- **Luca**, 23 anni, youtuber e creatore di short form content, cerca materiale breve e aggiornato riguardante gli ultimi sviluppi sui temi più attivi nel dibattito scientifico. 

___

### Modello di fruizione

il prodotto creato deve essere in un formato che sia ampiamente utilizzato e aggiornabile, e che sia adatto alla pubblicazione sul web. 

la fruizione del contenuto deve essere chiara e accessibile, si deve ottenere un modello di lettura _testuale_, dal tono rigoso, ma non eccessivamente scientifico, il progetto ha l'obbiettivo di rendere chiaro ad un pubblico più ampio il punto degli articoli pubblicati,  per questo è possibile introdurre anche _degli elementi  visuali_ come grafici e diagrammi tratti da essi.  

### Canali di distribuzione

| Canale                                | Formato         | In che modo                                        |
| ------------------------------------- | --------------- | -------------------------------------------------- |
| Web                                   | HTML            | pubblicazione sul sito EdiNews, con framework hugo |
| Social / newsletter                   | Estratti + link | è possibile ottenere il materiale in .md dal sito  |
| lettura offline/embedding in siti web | PDF             | Conversione in pdf del contenuto, stampabile       |

L’identità visiva è minimale, con uso di stili coerenti L’impaginazione segue modelli editoriali classici delle riviste scientifiche divulgative, ispirato a siti come: 
https://theconversation.com/global

lo stile deve essere formale e ispirare affidabilità in chi ne fruisce, è stato preferito quindi l'utilizzo modelli già presenti sul mercato. 

adattabile a dispositivi mobile. 

## Processo di Produzione

### Acquisizione dei contenuti

le fonti utilizzate per redigere il materiale sono articoli scientifici con licenza open access.

prima dell'effettiva ricerca è fondamentale analizzare gli argomenti più rilevanti nel dibattito pubblico attraverso strumenti come __google trends.__

la ricerca delle fonti sull'argomento è stata effettuata su [Google Scholar](https://scholar.google.com/) è stato così possibile selezionare riviste scientifiche che espongono articoli con licenza libera, come [ScienceDirect](https://www.sciencedirect.com/)


altre fonti libere possono essere [Zenodo](https://zenodo.org/) e [PubMed](https://pubmed.ncbi.nlm.nih.gov/), ma ho avuto difficoltà a trovare articoli che riguardassero lo stesso argomento, restano comunque valide alternative per la ricerca. 

per processo di creazione dei contenuti è necessario un lavoro di _redazione manuale_, per la stesura di un file Markdown o di testo che contenga la sintesi/analisi dei documenti raccolti, documento che necessita l'inserimento di appropriati metadati in stile yaml

è in teoria possibile generare un'introduzione per l'articolo che raccolga i principali punti chiave degli argomenti automaticamente, tramite AI. 

### Gestione documentale

```mermaid
graph LR
    H[Analisi trends] --> A[Ricerca papers]
    A[Ricerca papers] --> B{la fonte è open access?}
    B --> |sì| C[creazione contenuto]
    B --> |no| A
    C --> D[Creazione file .md per pubblicazione]
    G[aggiunta metadati yaml] --> C
    C --> E[creazione pdf con pandoc]
    D --> F
    E --> F((Caricamento Materiali con hugo))
```

### Tecnologie adottate

| Tecnologia  | Utilizzo                                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------------------------- |
| Markdown    | Scrittura modulare, leggibile, aggiornabile, facilmente modificabile da più persone durante la stesura del contenuto. |
| Yaml        | Metadati (autore, tag, abstract), Parametrizzare trasformazioni                                                       |
| pandoc      | Conversione formati (PDF)                                                                                             |
| Python/bash | Script per automatizzare build                                                                                        |
| Git/GitHub  | Gestione versioning + pubblicazione su GitHub pages                                                                   |

### Esecuzione del flusso

[repository del progetto](https://github.com/voksDB/esercizio_editoria_EdiNews)

___

## Valutazione dei risultati raggiunti

### Valutazione del flusso di produzione


L'introduzione di script per la generazione e pubblicazione dei documenti ha permesso una riduzione nella preparazione del materiale, in particolare nelle fasi ripetitive come:
- generazione dei file md strutturati per la pubblicazione
- generazione dei file PDF 
- pubblicazione automatica tramite GitHub Pages

L’adozione di standard aperti e di strumenti semplici da usare ha facilitato la portabilità del progetto su diverse piattaforme. 
 
### Confronto con lo stato dell'arte

nelle prossime versioni si potrebbe migliorare l'integrazione dell'utilizzo dei metadati nell'indicizzazione delle notizie, nel sito la ricerca degli articoli potrebbe avvenire tramite i tag associati nei metadati. 

si potrebbe implementare un controllo tramite AI sul tono, sul lessico e sulla grammatica del linguaggio usato nelle sintesi degli articoli. 


### Limiti emersi

dato l'obbiettivo di fornire aggiornamenti in tempo rapido, una delle principali difficoltà è stabilire l'adeguato _rapporto tra rapidità e qualità delle informazioni_

 La  _ricerca automatizzata delle fonti open access_ è complessa: gli articoli scientifici cercati sono distribuiti su piattaforme diverse, senza API standardizzate per il recupero delle fonti. 

## Conclusioni

Il progetto ha dimostrato la l’utilità di produrre un contenuto editoriale digitale, orientato a giornalisti e comunicatori, capace di sintetizzare risultati scientifici in modo rigoroso ma accessibile.

obiettivi principali raggiunti:
- produzione di contenuti affidabili, aggiornabili, verificabili
- aggiornabilità, portabilità e semplicità di utilizzo tramite markdown e hugo
- automazione di parte del flusso documentale

## Bibliografia e sitografia

[jain2022hugo,@heath2025navigating,@mezieobi2025strategies,@mccall2025locating]