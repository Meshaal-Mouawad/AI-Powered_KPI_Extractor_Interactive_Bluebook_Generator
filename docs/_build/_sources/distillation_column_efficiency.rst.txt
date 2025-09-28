Distillation Column Efficiency %
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_06.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_06.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Distillation%20Column%20Efficiency%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Distillation Column Efficiency % measures the effectiveness of a distillation column in separating components based on their volatility</li><li>It is calculated by comparing the number of theoretical stages required for separation to the actual stages achieved during operation</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to evaluate the performance of the distillation column</li><li>ensuring optimal separation efficiency and identifying potential areas for improvement in the distillation process</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The KPI is derived by dividing the number of theoretical stages by the actual stages, with the result multiplied by 100 to express it as a percentage.</p>
               <div class="math-equation">$$ \mathit{Distillation\,Column\,Efficiency\,\%} = \mathit{0))} \times \mathit{100} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               8.9s (AI 8.9s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 8.869s
                  • AI: 8.869s
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
            <td><ul><li>This KPI is utilized in performance monitoring and optimization of distillation processes within the oil</li><li>gas</li><li>and petrochemical industries</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the theoretical stages</li><li>which represent the ideal number of stages for separation</li><li>and the actual stages</li><li>which reflect the real operational performance of the distillation column</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for this KPI is percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI is typically derived from operational data collected during the distillation process.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher Distillation Column Efficiency % indicates better performance and effective separation, while a lower percentage may signal inefficiencies that could lead to increased operational costs.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Distillation Column Efficiency %
   SELECT (theoretical_stages / NULLIF(actual_stages,0)) * 100 AS [Distillation Column Efficiency %]
   FROM (SELECT 45.0 AS theoretical_stages, 50.0 AS actual_stages) c;