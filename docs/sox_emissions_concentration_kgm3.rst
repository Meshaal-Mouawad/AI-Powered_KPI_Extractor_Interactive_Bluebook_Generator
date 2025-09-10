SOx Emissions Concentration (kg/m3
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
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/lc_kpi.st:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/lc_kpi.st&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=SOx%20Emissions%20Concentration%20%28kg/m3" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>SOx Emissions Concentration measures the concentration of sulfur oxides in a given volume of gas</li><li>expressed in kilograms per cubic meter</li><li>This KPI is crucial for monitoring air quality and compliance with environmental regulations</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of tracking SOx Emissions Concentration is to ensure that emissions are kept within permissible limits</li><li>thereby minimizing environmental impact and adhering to regulatory standards</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The concentration is calculated by dividing the mass flow of sulfur oxides by the volumetric flow rate of the gas stream, providing a direct measure of pollutant concentration.</p>
               <div class="math-equation">$$ \mathit{Sox\,Conc} = \mathit{15\,2;\,(} \times \mathit{Pretend\,This\,Comes\,From\,An\,Analyzer\,Tag} \times \mathit{)} $$</div>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is utilized in various environmental performance assessments and compliance reporting frameworks to evaluate the effectiveness of emission control strategies</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The primary input measures for this KPI include the mass flow rate of sulfur oxides and the volumetric flow rate of the gas being analyzed</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for SOx Emissions Concentration is kilograms per cubic meter (kg/m3).</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for this KPI is typically sourced from continuous emissions monitoring systems (CEMS) or gas analyzers that provide real-time measurements of SOx emissions.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Regular monitoring of SOx Emissions Concentration is essential for identifying trends, ensuring compliance with environmental regulations, and implementing necessary corrective actions to reduce emissions.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: iecst
      :linenos:
   

      // KPI: SOx Emissions Concentration (kg/m3)
   VAR
       soxConc : REAL := 0.0;
       soxMassFlow : REAL := 0.0;
       volFlow : REAL := 0.0;
   END_VAR

   (* Example structured text placeholder *)
   soxConc := 15.2; (* pretend this comes from an analyzer tag *)
   soxMassFlow := 233.4;
   volFlow := 15.3;