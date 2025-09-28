Reactor Conversion %
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_03.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_03.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Reactor%20Conversion%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Reactor Conversion % measures the efficiency of a chemical reactor by calculating the percentage of feed material that has been converted into product</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to assess the performance of the reactor in converting raw materials into desired products</li><li>thereby optimizing production processes and maximizing yield</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The formula for Reactor Conversion % is derived by dividing the amount of converted material by the total feed amount, and then multiplying by 100 to express it as a percentage.</p>
               <p>See code context for implementation details.</p>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               50.2s (AI 50.2s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 50.21s
                  • AI: 50.21s
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
            <td><ul><li>This KPI is used in various performance metrics related to reactor efficiency</li><li>production optimization</li><li>and overall process effectiveness in the petrochemical industry</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the total amount of feed material introduced into the reactor and the amount of material that has been successfully converted</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Reactor Conversion % is percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI is typically derived from production data collected during the operation of the reactor.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A high Reactor Conversion % indicates effective reactor performance, while a low percentage may signal issues such as incomplete reactions or operational inefficiencies.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Reactor Conversion %
   SELECT 100.0 * (converted / NULLIF(feed,0)) AS [Reactor Conversion %]
   FROM (SELECT 950 AS converted, 1000 AS feed) a;