import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno is None or anno=='':
            self._view.create_alert("Inserire anno")
        try:
            int(anno)
        except ValueError:
            self._view.create_alert("Inserire valore NUMERICO")
            return
        if int(anno)< 1816 or int(anno) > 2016:
            self._view.create_alert("Inserire valore compreso tra 1816 e 2016")
            return
        self._model.buildGraph(int(anno))
        self._view._txt_result.controls.append(ft.Text(f'Grafo correttamente creato.'))
        self._view._txt_result.controls.append(ft.Text(f'Il grafo ha {self._model.getCompConnesse()} componenti connesse.'))
        self._view._txt_result.controls.append(ft.Text(f'Di seguito il dettaglio sui nodi:'))
        for i in self._model.getDegreeNodes():
            self._view._txt_result.controls.append(ft.Text(f'{i[0].StateNme}--{i[1]} vicini'))
        self._view._btnTrova .disabled=False
        self._view.update_page()

    def getStati(self):
        nodesOrdinati = sorted(self._model.getNations(), key=lambda x: x.StateNme)
        for i in nodesOrdinati:
            self._view._ddStati.options.append(ft.dropdown.Option(key=i.CCode, text=i.StateNme))

    def handleTrova(self, e):
        self._view._txt_result.controls.clear()
        idInput=self._view._ddStati.value
        conn= self._model.getConnections(int(idInput))
        self._view._txt_result.controls.append(ft.Text(f'{len(conn)}'))
        for i in conn:
            self._view._txt_result.controls.append(ft.Text(f'{i.StateNme}'))
        self._view.update_page()
