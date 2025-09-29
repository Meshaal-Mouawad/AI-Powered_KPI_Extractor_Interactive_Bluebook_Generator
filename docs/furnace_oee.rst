Furnace OEE %
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/plsql_kpi_02.pkb:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/plsql_kpi_02.pkb&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Furnace%20OEE%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Overall Equipment Effectiveness combines Availability</li><li>Performance</li><li>and Quality into a single effectiveness score</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>Increase effective productive time by reducing downtime</li><li>speed losses</li><li>and quality losses</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>Calculated directly from the inputs found in the code implementation.</p>
               <div class="math-equation">$$ \mathit{Function} = \mathit{} - \mathit{-\,Kpi\,Furnace\,Oee\,\%\,Create\,Or\,Replace\,Package\,Body\,Kpi\,Furnace} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               1m 6s (AI 1m 6s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 65.876s
                  • AI: 65.875s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI can serve as an input to higher-level operational and performance dashboards</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>Availability</li><li>performance</li><li>and quality factors calculated for the asset or line</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>%</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Operations data sources such as historians, SCADA/DCS tags, and production logs.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>No additional comments or special considerations were provided for this KPI.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Furnace OEE %
   CREATE OR REPLACE PACKAGE BODY kpi_furnace AS
     FUNCTION furnace_oee RETURN NUMBER IS
       availability NUMBER := 0.92;