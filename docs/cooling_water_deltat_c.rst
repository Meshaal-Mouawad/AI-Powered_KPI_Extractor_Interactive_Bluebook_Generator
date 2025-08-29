Cooling Water Delta-T (°C)
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:103" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=103" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Cooling Water Delta-T measures the temperature difference between the inlet and outlet of a cooling water system</li><li>This value is crucial for assessing the performance of heat exchangers within the plant</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The primary objective of monitoring Cooling Water Delta-T is to ensure optimal heat exchange efficiency and to identify potential issues such as fouling or scaling in the heat exchangers</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The Cooling Water Delta-T is calculated by subtracting the inlet temperature from the outlet temperature of the cooling water.</p>
               <div class="math-equation">$$ \mathit{Delta\,T} = \mathit{Outlet\,Temp} - \mathit{Inlet\,Temp} $$</div><ul><li>Outlet Temp: Value used in the calculation as defined by the code implementation.</li><li>Inlet Temp: Value used in the calculation as defined by the code implementation.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in various operational assessments and maintenance strategies to ensure the efficiency of cooling systems</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI are the inlet and outlet temperatures of the cooling water</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>tons/day</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is typically sourced from temperature sensors installed in the cooling water system.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A lower-than-expected Delta-T can indicate issues that may require maintenance or operational adjustments to maintain system efficiency.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 3
   

      def calculate_cooling_water_effectiveness(inlet_temp: float, outlet_temp: float) -> float:
       """Calculates the temperature difference, indicating heat exchanger performance."""
       # KPI: Cooling Water Delta-T (°C)
       # A lower-than-expected Delta-T can indicate fouling or scaling in heat exchangers.
       delta_t = outlet_temp - inlet_temp
       return delta_t

