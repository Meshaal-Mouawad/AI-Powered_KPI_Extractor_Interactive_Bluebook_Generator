Reactor Selectivity %
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/plsql_kpi_01.pkb:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/plsql_kpi_01.pkb&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Reactor%20Selectivity%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Reactor Selectivity % measures the efficiency of a chemical reactor in producing the desired product relative to undesired byproducts during a chemical reaction</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of monitoring Reactor Selectivity % is to optimize the reaction conditions to maximize the yield of the desired product while minimizing the formation of byproducts</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>Reactor Selectivity % is calculated by comparing the amount of desired product produced to the total amount of products formed, expressed as a percentage.</p>
               <div class="math-equation">$$ \mathit{Function} = \mathit{} - \mathit{-\,Kpi\,Reactor\,Selectivity\,\%\,Create\,Or\,Replace\,Package\,Body\,Kpi\,Pkg} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               0.0s (AI 0.0s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 0.001s
                  • AI: 0.001s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>100.0%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>0.0%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in performance assessments of chemical reactors and in the evaluation of process efficiency in petrochemical production</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measure for Reactor Selectivity % includes the quantities of desired and undesired products generated during the reaction</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Reactor Selectivity % is a percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI typically includes data from process control systems and laboratory analyses of product samples.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>High Reactor Selectivity % indicates effective reaction conditions and process optimization, while low selectivity may signal the need for adjustments in operating parameters.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Reactor Selectivity %
   CREATE OR REPLACE PACKAGE BODY kpi_pkg AS
     FUNCTION reactor_selectivity RETURN NUMBER IS
       desired NUMBER := 910;